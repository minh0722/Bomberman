import sys
import queue
import errno
from socket import *
from game_settings import *
from network_socket import NetworkSocket
from threading import Thread
from util import encode, decode
import time
from NetworkEvents import *


class Client:
    def __init__(self):
        self.socket = NetworkSocket()
        self.socket.connect(('localhost', PORT))

        self.is_connected = True

        self.socket.set_blocking(0)

        self.receive_thread = Thread()
        self.receive_thread.run = self._receive_packet_from_server
        self.receive_thread.start()

        self.incoming_packets = queue.Queue()

    def __del__(self):
        print("joining thread")
        self.receive_thread.join()
        self.socket.close_socket()

    def send_packet(self, packet):
        self.socket.send_all(encode(packet))

    def connected(self):
        return self.is_connected

    def _receive_packet_from_server(self):
        while True:
            try:
                packet = self.socket.recv()
                print(packet)

                if decode(packet) == Event.EXIT:
                    break

                elif decode(packet) == 'full':
                    print("Server full! Try again later!")
                    self.is_connected = False
                    break

                self.is_connected = True

            except Exception as e:
                pass

