#!/usr/bin/env python3
import time
import logging

from serial.threaded import LineReader
from commands import LoraCommands
from lora_stick import LoraStick
from utils import *

LOSTIK_PACKET_SIZE = 255

class Sender(LineReader):

    def setup_thread(self, rx_thread, interactive):
        self.rx_thread = rx_thread
        self.isInteractiveMode = interactive
        if not self.isInteractiveMode:
            receivePacket(self.tx)

    def connection_made(self, transport):
        logging.debug("[Sender] Connection Made")
        self.transport = transport
        self.antenna = LoraStick(self, "Sender")

    def handle_line(self, data):
        if data == LoraCommands.RADIO_DATA_OK:
            return
        logging.debug("[Sender] RECV: %s" % data)

    def connection_lost(self, exception):
        if exception:
            logging.error(exception)
        logging.debug("[Sender] Thread stopped")

    def tx(self):
        if self.isInteractiveMode:
            msg = input("Type a message to send: ")
        logging.debug("[Sender] Stopping reader thread")
        self.rx_thread.stop()
        self.antenna.send(msg)

    def send_cmd(self, command, delay=100):
        self.antenna.send_cmd(command, delay)
