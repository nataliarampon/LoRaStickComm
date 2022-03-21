#!/usr/bin/env python3
import time
import logging

from serial.threaded import LineReader
from commands import LoraCommands
from lora_stick import LoraStick
from utils import *
from serial.threaded import ReaderThread
from radio_receiver import *

LOSTIK_PACKET_SIZE = 255

class Sender(LineReader):

    def setup_thread(self, rx_thread, interactive, dest_ip = ""):
        self.rx_thread = rx_thread
        self.isInteractiveMode = interactive
        self.dest_ip = dest_ip
        logging.debug("Interactive mode: %s" % self.isInteractiveMode)
        # if not self.isInteractiveMode:
            # receivePacket(self.tx)

    def connection_made(self, transport):
        logging.debug("[Sender] Connection Made")
        self.transport = transport
        self.antenna = LoraStick(self, "Sender")

    def handle_line(self, data):
        if data == LoraCommands.RADIO_DATA_OK or data == LoraCommands.RADIO_LINE_BUSY:
            return
        if data == LoraCommands.RADIO_DATA_ERROR:
            self.antenna.enter_rx_mode()
            return

        logging.debug("[Sender] Data Received: %s" % data)
        try:
            if self.isInteractiveMode:
                bytes_data = self.antenna.decode_received_data(data)
                sendPacket(bytes_data, self.dest_ip)
            self.send_cmd(LoraCommands.SET_CONTINUOUS_RADIO_RECEPTION)
        except:
            logging.error("[Sender] Error decoding the received data [%s]" % data)

    def connection_lost(self, exception):
        if exception:
            logging.error(exception)
        logging.debug("[Sender] Thread stopped")

    def tx(self, message = ""):
        if self.isInteractiveMode:
            msg = input("Type a message to send: ")
        else:
            msg = message
        logging.debug("[Sender] Stopping reader thread")
        self.rx_thread.stop()
        self.antenna.send(msg)

        self.rx_thread = ReaderThread(self.rx_thread.serial, Receiver)
        self.rx_thread.start()
        self.rx_thread.protocol.setup_thread(self.isInteractiveMode, self.dest_ip)

    def send_cmd(self, command, delay=100):
        self.antenna.send_cmd(command, delay)
