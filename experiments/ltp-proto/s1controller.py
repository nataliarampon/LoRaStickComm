#!/usr/bin/env python2
import argparse, grpc, os, sys
from time import sleep
from scapy.all import *
from binascii import hexlify
import struct

# Import P4Runtime lib from parent utils dir
# Probably there's a better way of doing this.
sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 '../utils/'))
import p4runtime_lib.bmv2
from p4runtime_lib.switch import ShutdownAllSwitchConnections
import p4runtime_lib.helper

SWITCH_TO_HOST_PORT = 1
SWITCH_TO_SWITCH_PORT = 2

"""tag_cpu 0xfd => 0375 => 253"""
"""tag_def 0xfe => 0376 => 254"""

LTP_CPU = "\375"
LTP_DEF = "\376"
LTP = 0
DEV_ID = "\001"

EGRESS_PORT = 1 # ver variavel para popular a porta

def writeTagBuildRules(p4info_helper, sw, dev_id, tag_id, eth_src, ip_src, ip_dst, port):

    table_entry = p4info_helper.buildTableEntry(
        table_name="MyIngress.ipv4_lpm",
        match_fields={
            "hdr.ethernet.ethsrcAddr": eth_src,
            "hdr.ipv4.srcAddr": ip_src,
            "hdr.ipv4.dstAddr": ip_dst
        },
        action_name="MyIngress.tag_build",
        action_params={
            "dev_id": dev_id,
            "tag_id": tag_id,
            "port": port
        })
    sw.WriteTableEntry(table_entry)
    print "Installed LTP Build rule on {}: MyIngress.ipv4_lpm({}, {}, {}) => MyIngress.tag_build({}, {}, {})".format(
            sw.name, eth_src, ip_src, ip_dst,
            hexlify(str(dev_id)), hexlify(str(tag_id)), port
        )

def writeARPReply(p4info_helper, sw, dst_ip, dst_mac_addr, sw_port, sw_port_mac):

    table_entry = p4info_helper.buildTableEntry(
        table_name="MyIngress.dmac",
        match_fields={
            "hdr.ipv4.dstAddr": dst_ip
        },
        action_name="MyIngress.set_dmac",
        action_params={
            "dst_mac_addr": dst_mac_addr,
            "sw_port": sw_port,
            "sw_port_mac": sw_port_mac
            
        })
    sw.WriteTableEntry(table_entry)
    print "Installed Arp rule on {}: MyIngress.dmac({}) => MyIngress.set_dmac_port({},{},{})".format(
            sw.name, dst_ip, dst_mac_addr, hexlify(str(sw_port)), sw_port_mac
        )

def writeIpv4BuildRules(p4info_helper, sw, dev_id, tag_id, ip_src, ip_dst):

    table_entry = p4info_helper.buildTableEntry(
        table_name="MyIngress.tag_exact",
        match_fields={
            "hdr.tag.dev_id": dev_id,
            "hdr.tag.tag_id": tag_id
        },
        action_name="MyIngress.ipv4_build",
        action_params={
            "ip_src": ip_src,
            "ip_dst": ip_dst,
        })
    sw.WriteTableEntry(table_entry)
    print "Installed IPv4 Build rule on {}: MyIngress.tag_exact({}, {}) => MyIngress.ipv4_build({}, {})".format(
            sw.name, hexlify(str(dev_id)), hexlify(str(tag_id)), ip_src, ip_dst
        )

def readTableRules(p4info_helper, sw):
    """
    Reads the table entries from all tables on the switch.

    :param p4info_helper: the P4Info helper
    :param sw: the switch connection
    """
    print "----- Reading tables rules for {} -----".format(sw.name)
    for response in sw.ReadTableEntries():
        for entity in response.entities:
            entry = entity.table_entry
            # TODO For extra credit, you can use the p4info_helper to translate
            #      the IDs in the entry to names
            table_name = p4info_helper.get_tables_name(entry.table_id)
            print '%s: ' % table_name,
            for m in entry.match:
                print p4info_helper.get_match_field_name(table_name, m.field_id),
                print '%r' % (p4info_helper.get_match_field_value(m),),
            action = entry.action.action
            action_name = p4info_helper.get_actions_name(action.action_id)
            print '->', action_name,
            for p in action.params:
                print p4info_helper.get_action_param_name(action_name, p.param_id),
                print '%r' % p.value,
            print

def printCounter(p4info_helper, sw, counter_name, index):
    """
    Reads the specified counter at the specified index from the switch. In our
    program, the index is the tunnel ID. If the index is 0, it will return all
    values from the counter.

    :param p4info_helper: the P4Info helper
    :param sw:  the switch connection
    :param counter_name: the name of the counter from the P4 program
    :param index: the counter index (in our case, the tunnel ID)
    """
    for response in sw.ReadCounters(p4info_helper.get_counters_id(counter_name), index):
        for entity in response.entities:
            counter = entity.counter_entry
            print "%s %s %d: %d packets (%d bytes)" % (
                sw.name, counter_name, index,
                counter.data.packet_count, counter.data.byte_count
            )

def printGrpcError(e):
    print "gRPC Error:", e.details(),
    status_code = e.code()
    print "(%s)" % status_code.name,
    traceback = sys.exc_info()[2]
    print "[%s:%d]" % (traceback.tb_frame.f_code.co_filename, traceback.tb_lineno)

def main(p4info_file_path, bmv2_file_path):
    global LTP_CPU, LTP_DEF, LTP, DEV_ID, EGRESS_PORT

    arp_table = {}
    ip_cache = {}
    tag_cache = {}
    
    # Instantiate a P4Runtime helper from the p4info file
    p4info_helper = p4runtime_lib.helper.P4InfoHelper(p4info_file_path)

    try:
        # Create a switch connection object.
        # this is backed by a P4Runtime gRPC connection.
        # Also, dump all P4Runtime messages sent to switch to given txt files.
        s1 = p4runtime_lib.bmv2.Bmv2SwitchConnection(
            name='s1',
            address='127.0.0.1:50051',
            device_id=0,
            proto_dump_file='logs/s1-p4runtime-requests.txt')

        # Send master arbitration update message to establish this controller as
        # master (required by P4Runtime before performing any other write operation)
        s1.MasterArbitrationUpdate()

        # Install the P4 program on the switches
        s1.SetForwardingPipelineConfig(p4info=p4info_helper.p4info,
                                       bmv2_json_file_path=bmv2_file_path)
        print "Installed P4 Program using SetForwardingPipelineConfig on s1"

        # We need the multicast group to forward the packets when we don't
        # know the dst mac address. 
        """
        mc_group_entry = p4info_helper.buildMCEntry(
            mc_group_id = 1,
            replicas = {
                1:1,
                2:2,
                3:3
            })
        """
        # For now, we only need to output the packet to port 1.
        # Remember that port 2 is the switch egress_port, to
        # reach the other end of the tag_based mechanism
        
        mc_group_entry = p4info_helper.buildMCEntry(
            mc_group_id = 1,
            replicas = {
                2:2,
                3:3,
                4:4,
                5:5,
                6:6
            })
        s1.WritePRE(mc_group = mc_group_entry)
        print "Installed mgrp on s1."
        
        # TODO Uncomment the following two lines to read table entries
        #readTableRules(p4info_helper, s1)

        while True:
            print("Packet-in - BEFORE")
            packetin = s1.PacketIn()
            print("Packet-in - AFTER")
            if packetin.WhichOneof('update')=='packet':
                print("Packet-in message update received")

                metadata = packetin.packet.metadata 
                for meta in metadata:
                    metadata_id = meta.metadata_id 
                    value = meta.value 

                output_metadata = "\000\000"

                packet_orig=packetin.packet.payload
                packet_string = hexlify(packet_orig)
                print "Packet-in: {}".format((packet_string[:60] + '..') if len(packet_string) > 75 else packet_string)

                if packet_orig[0] == LTP_DEF:
                    print "Received LTP_DEF packet. Something is wrong..."

                elif  packet_orig[0] == LTP_CPU:
                    # This is a packet that has a LTP_CPU, indicating that it is the first packet of the tunnel, and along came with ether
                    # and ipv4 headers. We must use those headers to populate the tables in our switch, which is the second end of the tunnel

                    packet = packet_orig[4:] # packet without tag header (4 bytes long)
                    pkt = Ether(_pkt=packet)
                    
                    eth_src = pkt.getlayer(Ether).src 
                    eth_dst = pkt.getlayer(Ether).dst 
                    ether_type = pkt.getlayer(Ether).type
    
                    print "Received packet tag LTP_CPU from {} to {} ether_type {}".format(eth_src, eth_dst, ether_type)

                    if ether_type == 2048:
                        ip_src = pkt[IP].src
                        ip_dst = pkt[IP].dst

                        print "Received packet LTP_CPU with IPv4 header from {} to {}".format(ip_src, ip_dst)

                        DEVSRC_ID=packet_orig[1]
                        LTPSRC_ID=packet_orig[2]

                        if (ip_src, ip_dst) not in ip_cache and (ip_dst, ip_src) not in ip_cache:
                            print "The pair (ip_src {}, ip_dst {}) is not in ip_cache.".format(ip_src, ip_dst)
                            print "This is the request packet of the tunnel, arriving at the other end."

                            ip_cache.setdefault((ip_src, ip_dst), (DEVSRC_ID, LTPSRC_ID))
                            ip_cache.setdefault((ip_dst, ip_src), (DEVSRC_ID, LTPSRC_ID))

                            # This is the rule for the ipv4 forward table: it matches the tag, and has as action the ipv4_build, which strips the
                            # tag header and creates back the ether and ipv4 headers (using as eth_src the mac addres of the switch)
                            writeIpv4BuildRules(p4info_helper, sw=s1, dev_id=DEVSRC_ID, tag_id=LTPSRC_ID, ip_src=ip_src, ip_dst=ip_dst)

                        else:
                            print "The pair (ip_src {}, ip_dst {}) ALREADY EXISTS in ip_cache. Something is wrong...".format(ip_src, ip_dst)

                else:
                    # This is the first packet of the one-way tunnel, without a tag. We must use the ether and ipv4
                    # headers to populate the tables we have in our switch
                    pkt = Ether(_pkt=packet_orig)
                    
                    eth_src = pkt.getlayer(Ether).src 
                    eth_dst = pkt.getlayer(Ether).dst 
                    ether_type = pkt.getlayer(Ether).type

                    print "Received standard packet from {} to {} ether_type {}".format(eth_src, eth_dst, ether_type)
                    if ether_type == 2048:
                        ip_src = pkt[IP].src
                        ip_dst = pkt[IP].dst
                        proto = pkt[IP].proto

                        print "Received IPv4 packet (proto {}) from {} to {}".format(proto, ip_src, ip_dst)

                        # learn ip to mac address and switch port (we assume they are static)
                        if ip_src not in arp_table:
                            print "ip_src {} not in arp_table. writing in the switch dmac table".format(ip_src)
                            arp_table.setdefault(ip_src, (eth_src, value, eth_dst))

                            # This is the rule for the dmac forward table: it will be used to match the packet on
                            # the way back, when building the ether and ipv4 headers, to populate the packet with
                            # the correct mac destination address. If there is no mac, we set the bcast address
                            # and send the packet to the multicast group
                            writeARPReply(p4info_helper, sw=s1, dst_ip=ip_src, dst_mac_addr=eth_src, sw_port=value, sw_port_mac=eth_dst)
                        
                        if (ip_src, ip_dst) not in ip_cache and (ip_dst, ip_src) not in ip_cache:
                            print "The pair (ip_src {}, ip_dst {}) is not in ip_cache.".format(ip_src, ip_dst)
                            print "This is the request packet of the tunnel, leaving the first end."
                            
                            DEVSRC_ID=DEV_ID
                            LTP=LTP + 1
                            LTPSRC_ID=LTP

                            ip_cache.setdefault((ip_src, ip_dst), (DEVSRC_ID, LTPSRC_ID))
                            ip_cache.setdefault((ip_dst, ip_src), (DEVSRC_ID, LTPSRC_ID))

                            # This is the rule for the tag forward table: it matches the pair ip_src and ip_dst, and has as action the tag_build, which
                            # strips the ether and ipv4 headers and places the tag header in the packet.
                            writeTagBuildRules(p4info_helper, sw=s1, dev_id=DEVSRC_ID, tag_id=LTPSRC_ID, eth_src=eth_src, ip_src=ip_src, ip_dst=ip_dst, port=EGRESS_PORT)

                            # This is the rule for the ipv4 forward table: it matches the tag, and has as action the ipv4_build, which strips the
                            # tag header and creates back the ether and ipv4 headers (using as eth_src the mac addres of the switch)
                            writeIpv4BuildRules(p4info_helper, sw=s1, dev_id=DEVSRC_ID, tag_id=LTPSRC_ID, ip_src=ip_dst, ip_dst=ip_src)

                            output_metadata = "\000" + LTP_CPU

                        else:
                            print "The pair (ip_src {}, ip_dst {}) already exists.".format(ip_src, ip_dst)
                            print "This is the reply packet of the tunnel."

                            # This is the rule for the tag forward table: it matches the pair ip_src and ip_dst, and has as action the tag_build, which
                            # strips the ether and ipv4 headers and places the tag header in the packet.
                            writeTagBuildRules(p4info_helper, sw=s1, dev_id=DEVSRC_ID, tag_id=LTPSRC_ID, eth_src=eth_src, ip_src=ip_src, ip_dst=ip_dst, port=EGRESS_PORT)

                            output_metadata = "\000" + LTP_DEF

                print "Preparing PacketOut"
                packetout = p4info_helper.buildPacketOut(
                    payload = packet_orig,
                    metadata = {
                        1: output_metadata
                    }
                )
                print "Sending PacketOut"
                s1.PacketOut(packetout)
                print "Finished PacketOut"

                print "arp_table:%s" % arp_table
                print "ip_cache:%s" % ip_cache
                print "=========================\n"
                
    except KeyboardInterrupt:
        print " Shutting down."
    except grpc.RpcError as e:
        printGrpcError(e)

    ShutdownAllSwitchConnections()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='P4Runtime Controller')
    parser.add_argument('--p4info', help='p4info proto in text format from p4c',
                        type=str, action="store", required=False,
                        default='./build/ltp_proto.p4.p4info.txt')
    parser.add_argument('--bmv2-json', help='BMv2 JSON file from p4c',
                        type=str, action="store", required=False,
                        default='./build/ltp_proto.json')
    args = parser.parse_args()

    if not os.path.exists(args.p4info):
        parser.print_help()
        print "\np4info file not found: %s\nHave you run 'make'?" % args.p4info
        parser.exit(1)
    if not os.path.exists(args.bmv2_json):
        parser.print_help()
        print "\nBMv2 JSON file not found: %s\nHave you run 'make'?" % args.bmv2_json
        parser.exit(1)
    main(args.p4info, args.bmv2_json)
