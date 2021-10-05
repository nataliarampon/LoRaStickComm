#!/usr/bin/env python3
import time

from serial.threaded import LineReader
from commands import LoraCommands

class Sender(LineReader):

    def setup_thread(self, rx_thread, socket):
        self.rx_thread = rx_thread
        self.socket = socket
    #     self.lock = lock

    def connection_made(self, transport):
        print("connection made")
        self.transport = transport
        self.send_cmd(LoraCommands.TURN_ON_LED)
        self.send_cmd(LoraCommands.GET_VERSION)
        self.send_cmd(LoraCommands.GET_RADIO_MODE)
        self.send_cmd(LoraCommands.GET_RADIO_FREQUENCY)
        self.send_cmd(LoraCommands.GET_RADIO_SPREADING_FACTOR)
        self.send_cmd(LoraCommands.START_RADIO_OP)
        self.send_cmd(LoraCommands.SET_RADIO_POWER.format(10))
        self.send_cmd(LoraCommands.TURN_ON_LED)

    def handle_line(self, data):
        if data == LoraCommands.RADIO_DATA_OK:
            return
        print("RECV: %s" % data)

    def connection_lost(self, exc):
        if exc:
            print(exc)
        print("port closed")

    def tx(self):
        msg = input("type a message to send: ")
        # socket_msg = socket.recv(255)
        # self.lock.acquire()
        self.rx_thread.stop()
        self.send_cmd(LoraCommands.TURN_OFF_LED) # Turn off LED during transmitting
        txmsg = LoraCommands.RADIO_DATA_TRANSFER.format(msg.encode("utf-8").hex())
        # txmsg = RADIO_DATA_TRANSFER.format(socket_msg.hex())
        self.send_cmd(txmsg)
        self.send_cmd(LoraCommands.TURN_ON_LED)
        # self.lock.release()

    def send_cmd(self, cmd, delay=.5):
        print("SEND: %s" % cmd)
        self.write_line(cmd)
        time.sleep(delay)
