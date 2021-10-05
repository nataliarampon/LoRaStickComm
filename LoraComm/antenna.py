#!/usr/bin/env python3

class Antenna(object):

    def setup(self):
        raise NotImplementedError("Antenna setup method not implemented")
    
    def enter_rx_mode(self):
        raise NotImplementedError("Antenna enter_rx_mode method not implemented")
    
    def enter_tx_mode(self):
        raise NotImplementedError("Antenna enter_tx_mode method not implemented")
    
    def send(self, data):
        raise NotImplementedError("Antenna send method not implemented")
    
    def decode_received_data(self, data):
        raise NotImplementedError("Antenna decode_received_data method not implemented")