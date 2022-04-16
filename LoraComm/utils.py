#!/usr/bin/env python3

import socket
import sys
import logging
import random
import threading

from scapy.all import IP, UDP, TCP, Ether, get_if_hwaddr, get_if_addr, get_if_list, sendp, AsyncSniffer, sniff, bytes_hex, hex_bytes, Packet

UDP_PROTOCOL = 1
TCP_PROTOCOL = 2
PORT_NUMER = 1
SWITCH_INTERFACE = "s1-eth" + str(PORT_NUMER)

def keep_alive():
    return

def get_if():
    iface = None	# Example of interface name for mininet switches: s1-eth1
    for interface in get_if_list():
        if SWITCH_INTERFACE in interface:
            iface = interface
            break;
    if not iface:
        logging.debug("Cannot find eth interface in any host")
        exit(1)
    return iface

def sendPacket(raw_packet):
    iface = get_if()
    logging.debug("Sending on interface [%s]" % iface)
    packet = Ether(raw_packet)
    # packet.show2()
    sendp(packet, iface = iface, verbose = False)

def receivePacket(tx_function):
    iface = get_if()
    logging.debug("Sniffing interface: [%s]" % iface)
    s = AsyncSniffer(iface = iface, prn = lambda pkt: handle_pkt(pkt, tx_function, iface))
    s.start()
    

def handle_pkt(packet, tx_function, iface):
    if IP in packet:
        # Ignore packets emitted to host
        #if get_if_addr(iface) == packet[IP].dst:
        if "10.0.1.1" == packet[IP].dst:
            return
    tx_function(bytes_hex(packet))
