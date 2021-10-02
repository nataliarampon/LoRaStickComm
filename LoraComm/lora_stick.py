#!/usr/bin/env python3

from commands import *

class LoraStick(Antenna):

    def __init__(self, transport):
        self.transport = transport

    def setup(self, transport):
        self.send_cmd(GET_VERSION)
        self.send_cmd(START_RADIO_OP)
        self.send_cmd(SET_RADIO_POWER.format(10))
    
    def enter_rx_mode(self):
        self.send_cmd(START_RADIO_OP)
        self.send_cmd(DISABLE_TIMEOUT)
        self.send_cmd(SET_CONTINUOUS_RADIO_RECEPTION)
    
    def enter_tx_mode(self)
        self.send_cmd(START_RADIO_OP)

    def send(self, data):
        txmsg = RADIO_DATA_TRANSFER.format(msg.encode("utf-8").hex())
        self.send_cmd(txmsg)
    
    def decode_received_data(self, data):
        if data.find(RADIO_RADIO_DATA_RECEIVED) == 0:
          data = data.split(' ', 1)[1].strip()
          print("message received: {} ({})".format(data, bytes.fromhex(data).decode("utf-8")))
        time.sleep(.1)
    
    def send_cmd(self, cmd, delay=.5):
        self.transport.write(('%s\r\n' % cmd).encode('UTF-8'))
        time.sleep(delay)