#!/usr/bin/env python3
import serial
import argparse
import socket
import time

from serial.threaded import ReaderThread

from radio_receiver import *
from radio_sender import *

logging.basicConfig(level=logging.DEBUG)
parser = argparse.ArgumentParser(description='LoRa Radio mode receiver.')
parser.add_argument('port', help="Receiving serial port descriptor")
args = parser.parse_args()

# socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0)
# socket.bind(("lo", 0))  # Check which address should be used

serial = serial.Serial(args.port, baudrate=57600)

thread_rx = ReaderThread(serial, Receiver)
thread_rx.start()
thread_rx.protocol.setup_thread(socket)

time.sleep(4);

thread_tx = ReaderThread(serial, Sender)
thread_tx.start()
thread_tx.protocol.setup_thread(thread_rx, socket)

time.sleep(4);

while(1):
    thread_tx.protocol.tx()
    thread_rx = ReaderThread(serial, Receiver)
    thread_rx.start()
    thread_rx.protocol.setup_thread(socket)
