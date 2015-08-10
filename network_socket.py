from socket import *
import sys
from game_settings import *


class NetworkSocket():
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self, server_address):
        self.socket.bind(server_address)

    def connect(self, server_address):
        self.socket.connect(server_address)

    def listen(self):
        self.socket.listen(1)

    def accept(self):
        return self.socket.accept()

    def close_socket(self):
        self.socket.close()

    def receive(self):
        return self.socket.recv(self.MAX_DATA_LEN)

    def send_all(self, message):
        self.socket.sendall(message)

    def recv(self, len):
        return self.socket.recv(len)
