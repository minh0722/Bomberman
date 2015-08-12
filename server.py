from socket import *
import sys
from game_settings import *
from network_socket import NetworkSocket
from util import decode


class Server:
    def __init__(self):
        self.socket = NetworkSocket()
        self.socket.bind(('localhost', PORT))
        self.socket.set_blocking(0)

        self.max_players = MAX_PLAYERS

        self.connected_sockets = list()

    def run(self):
        self.socket.listen(MAX_CONNECTION)

        print('waiting for a connection')

        while True:
            self._serve_players()

            if len(self.connected_sockets) < self.max_players:
                try:
                    connection_socket, client_address = self.socket.accept()
                except error:
                    continue
                print("connection established with ", client_address[0])
                connection_socket.setblocking(0)
                self.connected_sockets.append(connection_socket)


    def _serve_players(self):
        for socket in self.connected_sockets:
            try:
                data = socket.recv(MAX_DATA_LEN)
            except error:
                continue
            print("received ", data)
            socket.sendall("asdqwe".encode('utf-8'))

    def __del__(self):
        self.socket.close_socket()

        for socket in self.connected_sockets:
            socket.close()
            print("closing server connection socket")

s = Server()
s.run()
