from argparse import ArgumentParser
from serial import Serial
from serial.threaded import LineReader, ReaderThread
from time import sleep
from sys import exit

DELAY: float = 0.5

parser = ArgumentParser(description='LoRa Radio mode sender.')
parser.add_argument('port', help='serial port descriptor')
args = parser.parse_args()


class Radio(LineReader):
    def __init__(self):
        super(Radio, self).__init__()

    def connection_made(self, transport):
        super(Radio, self).connection_made(transport)
        print('[INIT] connection established.')
        print('[INIT] configuring...')
        self.send_cmd('sys set pindig GPIO10 0')
        self.send_cmd('sys set pindig GPIO11 0')
        self.send_cmd('mac pause')
        self.send_cmd('radio set pwr 10')
        print('[INIT] done.')

    # It needs to implement this abstract method.
    def handle_line(self, data):
        pass

    def connection_lost(self, exception):
        super(Radio, self).connection_lost(exception)
        print('[FINISHED] connection closed.')

    def switch(self):
        for i in range(0, 3):
            # Transmit
            print(f'[STATUS] transmission {(i + 1):02}')
            self.send_cmd('sys set pindig GPIO10 1')
            self.send_cmd('sys set pindig GPIO11 0')
            self.send_cmd('radio tx test')
            sleep(DELAY)
            # Receive
            print(f'[STATUS] reception {(i + 1):02}')
            self.send_cmd('sys set pindig GPIO10 0')
            self.send_cmd('sys set pindig GPIO11 1')
            self.send_cmd('radio rx 0')
            sleep(DELAY)

    def send_cmd(self, command):
        self.write_line(command)
        print(f'[COMMAND SENT] {command}')
        sleep(DELAY)


ser = Serial(args.port, baudrate=57600)
with ReaderThread(ser, Radio) as protocol:
    protocol.switch()
    raise KeyboardInterrupt
exit(0)
