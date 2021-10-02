#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0)
s.bind(("lo", 0))

src_addr = "\x01\x02\x03\x04\x05\x06\x01\x02\x03\x04\x05\x06\x01\x02"

s.send (src_addr)

