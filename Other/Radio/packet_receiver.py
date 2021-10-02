import socket


class PacketReceiver:
    def __init__(self):
        self._sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

    def bind(self, interface: str):
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, interface.encode('utf-8'))

    def receive(self, max_bytes: int):
        return self._sock.recvfrom(max_bytes)


if __name__ == '__main__':
    import sys

    INTERFACE: str = 'enp0s3'
    MAX_BYTES: int = 65565

    sniffer: PacketReceiver = PacketReceiver()
    sniffer.bind(INTERFACE)
    pkt_count: int = 0
    while True:
        try:
            print(f'[RECEIVED] {(pkt_count + 1):03}: {sniffer.receive(MAX_BYTES)}')
            pkt_count += 1
        except KeyboardInterrupt:
            print(f'\n[FINISHED] received {pkt_count} packets.')
            sys.exit(0)
