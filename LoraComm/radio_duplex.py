#!/usr/bin/env python3
import serial
import argparse
import time

from serial.threaded import ReaderThread

from radio_receiver import *
from radio_sender import *

TEST_HOST_IP ="10.0.2.2"

logging.basicConfig(level=logging.DEBUG)
parser = argparse.ArgumentParser(description='LoRa Radio mode receiver.')
parser.add_argument('port', help="Receiving serial port descriptor")
parser.add_argument('--interactive', action="store_true", default=False, help="Runs in interactive mode, sending messages provided through the terminal")
args = parser.parse_args()

serial = serial.Serial(args.port, baudrate=57600)

thread_rx = ReaderThread(serial, Receiver)
thread_rx.start()
thread_rx.protocol.setup_thread(args.interactive, TEST_HOST_IP)

time.sleep(4);

thread_tx = ReaderThread(serial, Sender)
thread_tx.start()
thread_tx.protocol.setup_thread(thread_rx, args.interactive)

time.sleep(4);

while(1):
    thread_tx.protocol.tx()
    thread_rx = ReaderThread(serial, Receiver)
    thread_rx.start()
    thread_rx.protocol.setup_thread()
