#!/usr/bin/env python3

import time
import logging
from serial.threaded import LineReader

from commands import LoraCommands
from lora_stick import LoraStick
from utils import *

class Receiver(LineReader):

    def setup_thread(self, interactive, dest_ip = ""):
        self.isInteractiveMode = interactive
        self.dest_ip = dest_ip

    def connection_made(self, transport):
        logging.debug("[Receiver] Connection Made")
        self.transport = transport
        self.antenna = LoraStick(self, "Receiver")
        self.antenna.setup()
        self.antenna.enter_rx_mode()
        self.send_cmd(LoraCommands.TURN_ON_RED_LED)

    def handle_line(self, data):
        if data == LoraCommands.RADIO_DATA_OK or data == LoraCommands.RADIO_LINE_BUSY:
            return
        if data == LoraCommands.RADIO_DATA_ERROR:
            self.antenna.enter_rx_mode()
            return

        logging.debug("[Receiver] Data Received: %s" % data)
        try:
            if self.isInteractiveMode:
                bytes_data = self.antenna.decode_received_data(data)
                sendPacket(bytes_data, self.dest_ip)
            self.send_cmd(LoraCommands.SET_CONTINUOUS_RADIO_RECEPTION)
        except:
            logging.error("[Receiver] Error decoding the received data [%s]" % data)

    def connection_lost(self, exception):
        if exception:
            logging.error(exception)
        logging.debug("[Receiver] Thread stopped")

    def send_cmd(self, command, delay=.5):
        self.antenna.send_cmd(command, delay)
