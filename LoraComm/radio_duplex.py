#!/usr/bin/env python3
"""
To-do: 
    []    2.2 - State machine to confirm successful transmission of each packet as per (rx_tx ACK)
    []        2.2.1 - Make sure the mac pause command works before starting whole thing ==> how to get response? there's a time limit to this mode (apparently 50 consecutive days for some reason), check for continous functionality
    []        2.2.2 - Distiction between ACKs from LoRa and actual received data (radio_rx)
    [] 3 - Pick up data and put into packet into socket  
"""
import time
import serial
import argparse 
import threading as thr
import socket

from serial.threaded import LineReader, ReaderThread

from commands import *
from radio_receiver import *
from radio_sender import *

parser = argparse.ArgumentParser(description='LoRa Radio mode receiver.')
parser.add_argument('port', help="Receiving serial port descriptor")
args = parser.parse_args()

socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0)
socket.bind(("lo", 0))  # Check which address should be used

# conn_lock = thr.Lock()

serial = serial.Serial(args.port, baudrate=57600)

thread_rx = ReaderThread(serial, Receiver)
thread_rx.setup_thread(socket)

thread_tx = ReaderThread(serial, Sender)
thread_tx.setup_thread(thread_rx)

while(1):
    thread_rx.run()
    thread_tx.tx()
