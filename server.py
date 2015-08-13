from socket import *
import sys
from game_settings import *
from network_socket import NetworkSocket
from util import decode, encode
from network_events import Event

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
                    print("SERVER_FULL sent successful...")
                except error as e:
                    print("Failed to send SERVER_FULL. exception raised: ", e)


    def _serve_players(self):
        for socket in self.connected_sockets:
            try:
                data = socket.recv(MAX_DATA_LEN)
            except error:
                continue

            if decode(data) != '' and decode(data) != Event.EXIT:
                if decode(data) == Event.START:
                    print("received ", data)
                    # try:
                    socket.sendall(encode(self._start_message()))
                    self._notify_other_sockets_except(
                        encode(Event.OTHER_PLAYER_JOINED),
                        socket)
                    # except BrokenPipeError:
                    #     self.connected_sockets.remove(socket)
                    #     print("removed broken socket in START")

                else:
                    print("received ", data)
                    # try:
                    socket.sendall(encode("asdqwe"))
                    # except BrokenPipeError:
                    #     self.connected_sockets.remove(socket)
                    #     print("removed broken socket")

            else:
                # send confirm to client
                socket.sendall(encode(Event.EXIT))
                self.connected_sockets.remove(socket)
                print("removed socket")

    def _start_message(self):
        connected_sockets_size = len(self.connected_sockets)
        return Event.START + " " + str(connected_sockets_size - 1)

    def _notify_other_sockets_except(self, message, socket):
        # send message to all sockets except the given one
        for sock in self.connected_sockets:
            if sock != socket:
                sock.sendall(message)

    def __del__(self):
        self.socket.close_socket()

        for socket in self.connected_sockets:
            socket.close()
            print("closing connected socket")

s = Server()
s.run()
