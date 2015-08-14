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

        self.generated_id = 0

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
                player_id = self._next_available_id()

                self.connected_sockets.append(
                    (connection_socket, str(player_id)))
            else:
                try:
                    connection_socket.sendall(encode(Event.SERVER_FULL))
                    print("SERVER_FULL sent successful...")
                except error as e:
                    print("Failed to send SERVER_FULL. exception raised: ", e)


    def _serve_players(self):
        for socket, player_id in self.connected_sockets:
            try:
                data = socket.recv(MAX_DATA_LEN)
            except error:
                continue

            print("received ", data)

            if decode(data) != '' and decode(data) != Event.EXIT:
                if decode(data) == Event.START:
                    self._handle_start_event(socket, player_id)
                else:
                    self._handle_player_events(socket, player_id, data)
            else:
                self._handle_exit_event(socket, player_id)


    def _handle_start_event(self, socket, player_id):
        socket.sendall(encode(self._get_start_message() + " " + player_id))

        self._notify_other_sockets_except(
            socket,
            encode(Event.OTHER_PLAYER_JOINED) + " " + player_id)

    def _handle_player_events(self, socket, player_id, data):
        message = Event.PLAYER + player_id + " " + Event.ACTION + decode(data)

        self._notify_other_sockets_except(
            socket,
            encode(message))

    def _handle_exit_event(self, socket, player_id):
        # send confirm to the exited client
        socket.sendall(encode(Event.EXIT))

        message_to_other_clients = Event.EXIT + " " + str(player_id)
        self._notify_other_sockets_except(socket, message_to_other_clients)

        for connection in self.connected_sockets:
            if connection[0] == socket:
                self.connected_sockets.remove(connection)
                break

        print("removed socket")        

    def _notify_other_sockets_except(self, socket, message):
        # send message to all sockets except the given one
        for sock, player_id in self.connected_sockets:
            if sock != socket:
                sock.sendall(message)

    def _get_start_message(self):
        # return start_event + current players count
        connected_sockets_size = len(self.connected_sockets)
        return Event.START + " " + str(connected_sockets_size - 1)

    def _next_available_id(self):
        if self.generated_id + 1 > MAX_PLAYERS:
            self.generated_id = 1
            return self.generated_id

        self.generated_id += 1
        return self.generated_id

    def __del__(self):
        self.socket.close_socket()

        for socket, player_id in self.connected_sockets:
            socket.close()
            print("closing connected socket")

s = Server()
s.run()
