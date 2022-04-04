#!/usr/bin/env python3

import socket
import sys
import logging
import random

from scapy.all import IP, UDP, TCP, Ether, get_if_hwaddr, get_if_list, sendp, AsyncSniffer

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
        logging.debug("Cannot find eth1 interface in any host")
        exit(1)
    return iface

def sendPacket(message, dest_ip, protocol = UDP_PROTOCOL):
    addr = socket.gethostbyname(dest_ip)
    iface = get_if()
    logging.debug("Sending on interface %s to %s" % (iface, str(addr)))

    pkt = Ether(src = get_if_hwaddr(iface), dst = MAC_BROADCAST)
    pkt = pkt / IP(dst = addr)
    if protocol == UDP_PROTOCOL:
        pkt = pkt / UDP(dport = 1234, sport = random.randint(49152,65535))
    else:
        pkt = pkt / TCP(dport = 1234, sport = random.randint(49152,65535))
    pkt = pkt / message
    pkt.show2()
    sendp(pkt, iface = iface, verbose = False)

def receivePacket(tx_function, protocol = UDP_PROTOCOL):
    iface = get_if()
    AsyncSniffer(iface = iface, prn = lambda pkt: handle_pkt(pkt, tx_function, iface, protocol))

def handle_pkt(packet, tx_function, iface, protocol = UDP_PROTOCOL):
    if IP in packet:
        # Ignore packets emitted from same MAC
        if get_if_hwaddr(iface) == packet[Ether].src:
            return

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        if protocol == UDP_PROTOCOL and UDP in packet:
            tx_function(packet[UDP].payload)

        if protocol == TCP_PROTOCOL and TCP in packet:
            tx_function(packet[TCP].payload)
