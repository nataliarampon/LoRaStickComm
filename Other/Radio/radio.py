from serial import Serial
from serial.threaded import LineReader
from packet_receiver import PacketReceiver
from sys import exit
from time import sleep

MAX_BYTES: int = 64
DELAY: float = 0.5


class Radio(LineReader):
    def __init__(self):
        super(Radio, self).__init__()
        self.sniffer = PacketReceiver()

    def connection_made(self, transport):
        super(Radio, self).connection_made(transport)
        print('[CONNECTION] established connection with the antenna.')
        print('[INIT] initializing...')
        self.send_cmd('sys set pindig GPIO10 1')
        self.send_cmd('sys set pindig GPIO11 1')
        self.send_cmd('mac pause')
        self.send_cmd('radio set pwr 10')
        print('[INIT] done.')

    def connection_lost(self, exception):
        super(Radio, self).connection_lost(exception)
        print('[CONNECTION] closed connection with the antenna.')
        self.send_cmd('sys set pindig GPIO10 0')
        self.send_cmd('sys set pindig GPIO11 0')

    def handle_line(self, line):
        pass

    # To be used with threading because it's a blocking I/O operation.
    def listen(self):
        return self.sniffer.receive(MAX_BYTES)

    def send_cmd(self, command):
        print('[COMMAND] {command}')
        self.write_line(command)
        sleep(DELAY)


def message_mode(port: str):
    print('[STARTED] initializing message reception/transmission...')


def packet_mode(interface: str, port: str):
    print('[STARTED] initializing packet reception...')

    radio = Radio()
    radio.sniffer.bind(interface)
    pkt_count = 0
    while True:
        try:
            print(f'[RECEIVED] {pkt_count + 1:03}: {radio.sniffer.receive(MAX_BYTES)}')
            pkt_count += 1
        except KeyboardInterrupt:
            print(f'\n[FINISHED] received {pkt_count} packets')
            exit()


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser: ArgumentParser = ArgumentParser()
    parser.add_argument('interface', action='store', type=str,
                        help='sniffer network interface')
    parser.add_argument('port', action='store', type=str,
                        help='antenna serial port')
    parser.add_argument('-m', '--message', action='store_true',
                        help='start the radio in message mode')

    args = parser.parse_args()
    if args.message:
        message_mode(args.port)
    else:
        packet_mode(args.interface, args.port)
