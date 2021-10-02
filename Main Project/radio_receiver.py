#!/usr/bin/env python3
import time
import serial
import argparse 

import socket

from serial.threaded import LineReader, ReaderThread

parser = argparse.ArgumentParser(description='LoRa Radio mode receiver.')
parser.add_argument('port', help="Serial port descriptor")
args = parser.parse_args()

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0)
s.bind(("lo", 0))

class PrintLines(LineReader):

    @staticmethod
    def write_to_socket(self, packet):
        import socket
        pass

    def connection_made(self, transport):
        print("connection made")
        self.transport = transport
        self.send_cmd('sys get ver')
        self.send_cmd('mac pause')
        self.send_cmd('radio set pwr 10')
        self.send_cmd('radio rx 0')
        self.send_cmd("sys set pindig GPIO10 0")

    def handle_line(self, data):
        if data == "ok" or data == 'busy':
            return
        if data == "radio_err":
            self.send_cmd('radio rx 0')
            return
        
        self.send_cmd("sys set pindig GPIO10 1", delay=0)
        if data.find("radio_rx") == 0:
          data = data.split(' ', 1)[1].strip()
          print("message received: {} ({})".format(data, bytes.fromhex(data).decode("utf-8")))
          # s.send(data.decode("hex")) # send to socket the message we just received
        time.sleep(.1)
        self.send_cmd("sys set pindig GPIO10 0", delay=1)
        self.send_cmd('radio rx 0')

    def tx(self): #GPIO11 => LED Vermelho, #GPIO10 => LED Azul 
        self.send_cmd("sys set pindig GPIO11 1")
        # txmsg = 'radio tx %x%x' % (int(time.time()), self.frame_count)
        msg = input("type a message to send: ")
        txmsg = 'radio tx %s' % (msg.encode("utf-8").hex())
        self.send_cmd(txmsg)
        time.sleep(.3)
        self.send_cmd('radio rx 0')
        self.send_cmd("sys set pindig GPIO11 0")

    def connection_lost(self, exc):
        if exc:
            print(exc)
        print("port closed")

    def send_cmd(self, cmd, delay=.5):
        self.transport.write(('%s\r\n' % cmd).encode('UTF-8'))
        time.sleep(delay)

ser = serial.Serial(args.port, baudrate=57600)
with ReaderThread(ser, PrintLines) as protocol:
    while(1):
        protocol.tx()
        time.sleep(0)

