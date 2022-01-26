#!/usr/bin/env python3

import time
import logging
from serial.threaded import LineReader

from antenna import Antenna
from commands import LoraCommands

class LoraStick(Antenna):

    def __init__(self, line_reader: LineReader, communicator_type):
        self.line = line_reader
        self.communicator_type = communicator_type

    def setup(self):
        self.send_cmd(LoraCommands.GET_VERSION)
        self.send_cmd(LoraCommands.GET_RADIO_MODE)
        self.send_cmd(LoraCommands.GET_RADIO_FREQUENCY)
        self.send_cmd(LoraCommands.GET_RADIO_SPREADING_FACTOR)
        self.send_cmd(LoraCommands.START_RADIO_OP)
        self.send_cmd(LoraCommands.SET_RADIO_POWER.format(10))
    
    def enter_rx_mode(self):
        self.send_cmd(LoraCommands.DISABLE_TIMEOUT)
        self.send_cmd(LoraCommands.SET_CONTINUOUS_RADIO_RECEPTION)
    
    def enter_tx_mode(self):
        self.send_cmd(LoraCommands.START_RADIO_OP)

    def send(self, data):
        tx_msg = LoraCommands.RADIO_DATA_TRANSFER.format(data.encode("utf-8").hex())
        self.send_cmd(tx_msg)
    
    def decode_received_data(self, data):
        if data.find(LoraCommands.RADIO_RADIO_DATA_RECEIVED) == 0:
          data = data.split(' ', 1)[1].strip()
          logging.debug("[LoraStick] Message Received: {} ({})".format(data, bytes.fromhex(data).decode("utf-8")))
        bytes_data = bytes.fromhex(data)
        return bytes_data
    
    def send_cmd(self, command, delay=.5):
        logging.debug("[%s] SEND: %s" % (self.communicator_type, command))
        self.line.write_line(command)
        time.sleep(delay)