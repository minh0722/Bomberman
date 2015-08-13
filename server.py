from socket import *
import sys
from game_settings import *
from network_socket import NetworkSocket
from util import decode, encode
from NetworkEvents import *


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

            try:
                connection_socket, client_address = self.socket.accept()
            except error:
                continue

            print("connection established with ", client_address[0])
            
            if len(self.connected_sockets) < self.max_players:
                connection_socket.setblocking(0)
                self.connected_sockets.append(connection_socket)
            else:
                try:
                    connection_socket.sendall(encode(Event.SERVER_FULL))
                except error as e:
                    print("failed to send full event. exception raised: ", e)

                print("sending server full event successful...")

    def _serve_players(self):
        for socket in self.connected_sockets:
            try:
                data = socket.recv(MAX_DATA_LEN)
            except error:
                continue

            if decode(data) != '' and decode(data) != EVENT.EXIT:
                print("received ", data)
                try:
                    socket.sendall(encode("asdqwe"))
                except BrokenPipeError:
                    self.connected_sockets.remove(socket)
                    print("removed broken socket")
            else:
                # send confirm to client
                socket.sendall(encode(Event.EXIT))
                self.connected_sockets.remove(socket)
                print("removed socket")

    def __del__(self):
        self.socket.close_socket()

        for socket in self.connected_sockets:
            socket.close()
            print("closing connected socket")

s = Server()
s.run()
