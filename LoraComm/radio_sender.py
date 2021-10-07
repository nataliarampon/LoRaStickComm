#!/usr/bin/env python3
import time
import logging

from serial.threaded import LineReader
from commands import LoraCommands
from lora_stick import LoraStick

class Sender(LineReader):

    def setup_thread(self, rx_thread, socket):
        self.rx_thread = rx_thread
        self.socket = socket
    #     self.lock = lock

    def connection_made(self, transport):
        logging.debug("[Sender] Connection Made")
        self.antenna = LoraStick(transport)
        self.antenna.setup()

    def handle_line(self, data):
        if data == LoraCommands.RADIO_DATA_OK:
            return
        logging.debug("[Sender] RECV: %s" % data)

    def connection_lost(self, exception):
        if exception:
            logging.error(exception)
        logging.debug("[Sender] Port Closed")

    def tx(self):
        # msg = input("type a message to send: ")
        socket_msg = self.socket.recv(255)
        # with self.lock:
        # self.rx_thread.stop()
        # self.antenna.send(msg)
        self.antenna.send(socket_msg)

    def send_cmd(self, command, delay=.5):
        self.antenna.send_cmd(command, delay)
