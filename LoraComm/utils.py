#!/usr/bin/env python3

import socket
import sys
import logging
import random

from scapy.all import IP, UDP, TCP, Ether, get_if_hwaddr, get_if_addr, get_if_list, sendp, AsyncSniffer, sniff, bytes_hex, hex_bytes, Packet

UDP_PROTOCOL = 1
TCP_PROTOCOL = 2
MAC_BROADCAST = 'ff:ff:ff:ff:ff:ff'
HOST_INTERFACE = "eth0"

def keep_alive():
    return

def get_if():
    iface = None	# Example of interface name for mininet hosts: s1-eth1
    for interface in get_if_list():
        if HOST_INTERFACE in interface:
            iface = interface
            break;
    if not iface:
        logging.debug("Cannot find eth interface in any host")
        exit(1)
    return iface

def sendPacket(raw_packet, dest_ip, protocol = UDP_PROTOCOL):
    iface = get_if()
    logging.debug("Sending on interface [%s]" % iface)
    packet = Ether(raw_packet)
    packet.show2()
    sendp(packet, iface = iface, verbose = False)

def receivePacket(tx_function, protocol = UDP_PROTOCOL):
    iface = get_if()
    logging.debug("Sniffing interface: [%s]" % iface)
    s = AsyncSniffer(iface = iface, prn = lambda pkt: handle_pkt(pkt, tx_function, iface, protocol))
    s.start()

def handle_pkt(packet, tx_function, iface, protocol = UDP_PROTOCOL):
    if IP in packet:
        # Ignore packets emitted to host
        if get_if_addr(iface) == packet[IP].dst:
            return

        if protocol == UDP_PROTOCOL and UDP in packet:
            tx_function(bytes_hex(packet))

        if protocol == TCP_PROTOCOL and TCP in packet:
            tx_function(bytes_hex(packet))
