#!/usr/bin/env python3

import time
import serial
import argparse 

from serial.threaded import LineReader, ReaderThread
import threading

from commands import *

class Receiver(LineReader):

    def setup_thread(self, socket):
        self.socket = socket
    #     self.lock = lock

    def connection_made(self, transport):
        print("connection made")
        self.transport = transport
        self.send_cmd(GET_VERSION)
        self.send_cmd(START_RADIO_OP)
        self.send_cmd(SET_RADIO_POWER.format(10))
        self.send_cmd(DISABLE_TIMEOUT)
        self.send_cmd(SET_CONTINUOUS_RADIO_RECEPTION)

    def handle_line(self, data):
        if data == RADIO_DATA_OK or data == RADIO_LINE_BUSY:
            return
        if data == RADIO_DATA_ERROR:
            self.send_cmd(DISABLE_TIMEOUT)
            self.send_cmd(SET_CONTINUOUS_RADIO_RECEPTION)
            return
        
        self.send_cmd(TURN_OFF_LED, delay=0)
        if data.find(RADIO_RADIO_DATA_RECEIVED) == 0:
          data = data.split(' ', 1)[1].strip()
          print("message received: {} ({})".format(data, bytes.fromhex(data).decode("utf-8")))
        #   bytes_data = bytes.fromhex(data)
        #   self.socket.send(bytes_data)
        time.sleep(.1)
        self.send_cmd(TURN_ON_LED, delay=1)
        self.send_cmd(DISABLE_TIMEOUT)
        self.send_cmd(SET_CONTINUOUS_RADIO_RECEPTION)

    def connection_lost(self, exc):
        if exc:
            print(exc)
        print("port closed")

    def send_cmd(self, cmd, delay=.5):
        self.transport.write(('%s\r\n' % cmd).encode('UTF-8'))
        time.sleep(delay)
