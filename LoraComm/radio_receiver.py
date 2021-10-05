#!/usr/bin/env python3

import time
from serial.threaded import LineReader

from commands import *

class Receiver(LineReader):

    def setup_thread(self, socket):
        self.socket = socket
    #     self.lock = lock

    def connection_made(self, transport):
        print("connection made")
        self.transport = transport
        self.send_cmd(LoraCommands.GET_VERSION)
        self.send_cmd(LoraCommands.START_RADIO_OP)
        self.send_cmd(LoraCommands.SET_RADIO_POWER.format(10))
        self.send_cmd(LoraCommands.DISABLE_TIMEOUT)
        self.send_cmd(LoraCommands.SET_CONTINUOUS_RADIO_RECEPTION)

    def handle_line(self, data):
        if data == LoraCommands.RADIO_DATA_OK or data == LoraCommands.RADIO_LINE_BUSY:
            return
        if data == LoraCommands.RADIO_DATA_ERROR:
            self.send_cmd(LoraCommands.DISABLE_TIMEOUT)
            self.send_cmd(LoraCommands.SET_CONTINUOUS_RADIO_RECEPTION)
            return
        
        self.send_cmd(LoraCommands.TURN_OFF_LED, delay=0)
        if data.find(LoraCommands.RADIO_RADIO_DATA_RECEIVED) == 0:
          data = data.split(' ', 1)[1].strip()
          print("message received: {} ({})".format(data, bytes.fromhex(data).decode("utf-8")))
        #   bytes_data = bytes.fromhex(data)
        #   self.socket.send(bytes_data)
        time.sleep(.1)
        self.send_cmd(LoraCommands.TURN_ON_LED, delay=1)
        self.send_cmd(LoraCommands.DISABLE_TIMEOUT)
        self.send_cmd(LoraCommands.SET_CONTINUOUS_RADIO_RECEPTION)

    def connection_lost(self, exc):
        if exc:
            print(exc)
        print("port closed")

    def send_cmd(self, cmd, delay=.5):
        self.transport.write(('%s\r\n' % cmd).encode('UTF-8'))
        time.sleep(delay)
