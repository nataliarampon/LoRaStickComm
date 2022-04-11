#!/usr/bin/env python3

import time
import logging
from serial.threaded import LineReader

from commands import LoraCommands
from lora_stick import LoraStick
from utils import *

class Radio(LineReader):

    def setup_thread(self, dest_ip):
        self.dest_ip = dest_ip

    def connection_made(self, transport):
        logging.debug("[Receiver] Connection Made")
        self.transport = transport
        self.antenna = LoraStick(self, "Receiver")
        self.antenna.setup()
        self.antenna.enter_rx_mode()
        self.send_cmd(LoraCommands.TURN_ON_RED_LED)
        receivePacket(self.tx)

    def handle_line(self, data):
        logging.debug("[Receiver] Callback Received: %s" % data)
        if data == LoraCommands.RADIO_DATA_OK or data == LoraCommands.RADIO_LINE_BUSY:
            return
        if data == data == LoraCommands.RADIO_DATA_ERROR:
            self.antenna.setup()
            self.antenna.enter_rx_mode()
        if LoraCommands.RADIO_RADIO_DATA_RECEIVED not in data:
            return
        logging.debug("[Receiver] Data Received: %s" % data)
        
        bytes_data = ""
        try:
            bytes_data = self.antenna.decode_received_data(data)
        except:
            logging.error("[Receiver] Error decoding the received data [%s]" % data)
        sendPacket(bytes_data, self.dest_ip)
        self.send_cmd(LoraCommands.SET_CONTINUOUS_RADIO_RECEPTION)

    def tx(self, message = ""):
        self.antenna.send(message)

    def connection_lost(self, exception):
        if exception:
            logging.error(exception)
        logging.debug("[Receiver] Thread stopped")

    def send_cmd(self, command, delay=.5):
        self.antenna.send_cmd(command, delay)
