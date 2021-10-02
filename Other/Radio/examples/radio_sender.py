#!/usr/bin/env python3
import time
import serial
import argparse 

from serial.threaded import LineReader, ReaderThread

parser = argparse.ArgumentParser(description='LoRa Radio mode sender.')
parser.add_argument('port', help='serial port descriptor')
args = parser.parse_args()


class PrintLines(LineReader):
    def __init__(self):
        super().__init__()
        self.frame_count = 0

    def connection_made(self, transport):
        print('connection made')
        self.transport = transport
        self.send_cmd('sys set pindig GPIO11 0')
        self.send_cmd('sys get ver')
        self.send_cmd('radio get mod')
        self.send_cmd('radio get freq')
        self.send_cmd('radio get sf')
        self.send_cmd('mac pause')
        self.send_cmd('radio set pwr 10')
        self.send_cmd('sys set pindig GPIO11 0')
        self.frame_count += 1

    def handle_line(self, data):
        if data == 'ok':
            return
        print(f'RECV: {data}')

    def connection_lost(self, exc):
        if exc:
            print(exc)
        print('port closed')

    def tx(self):
        self.send_cmd('sys set pindig GPIO11 1')
        msg = input('type a message to send: ')
        txmsg = f'radio tx {msg.encode("hex")}'
        self.send_cmd(txmsg)
        time.sleep(.3)
        self.send_cmd('sys set pindig GPIO11 0')

    def send_cmd(self, cmd, delay=.5):
        print(f'SEND: {cmd}')
        self.write_line(cmd)
        time.sleep(delay)


ser = serial.Serial(args.port, baudrate=57600)
with ReaderThread(ser, PrintLines) as protocol:
    while True:
        protocol.tx()
        time.sleep(0)
