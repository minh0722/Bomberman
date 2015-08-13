import sys
import queue
from socket import *
from game_settings import *
from network_socket import NetworkSocket
from threading import Thread
from util import encode
import time


class Client:
    def __init__(self):
        self.socket = NetworkSocket()
        self.socket.connect(('localhost', PORT))

        self.socket.set_blocking(0)

        self.incoming_packets = queue.Queue()
        self.game_over = False

    def run(self):
        while True:
            _receive_packet_from_server()

    def send_packet(self, packet):
        self.socket.send_all(encode(packet))

    def set_game_over(self, is_game_over):
        self.game_over = is_game_over

    def _receive_packet_from_server(self):
        while True:
            packet = self.socket.recv()
            print(packet)
            if packet:
                self.incoming_packets.put(packet)
