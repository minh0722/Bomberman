from socket import *
import sys
from game_settings import *
from network_socket import NetworkSocket
from util import decode, encode, get_event_list
from network_events import Event
from player import Direction

# Start event = Event.START + players connected count + their id + their pos + this player's id
# player join = Event.OTHER_PLAYER_JOINED + that plsyer's id
# player action = Event.ACTION + the action that player took
# notify player exit = EVENT.EXIT + id of the exited player


class Server:
    def __init__(self):
        self.connected_sockets = list()

        self.socket = NetworkSocket()
        self.socket.bind((SERVER_BIND_ADDRESS, PORT))
        self.socket.set_blocking(0)

        self.max_players = MAX_PLAYERS

        self.generated_id = 0

        self.players_position = dict()

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
                self.players_position[str(player_id)] = (22, 0)

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

            events = get_event_list(decode(data))
            print("received ", events)

            if decode(data) != '':
                if events[0] == "start":
                    self._handle_start_event(socket, player_id)
                elif events[0] == "action":
                    self._handle_player_action_events(socket, player_id, events)

    def _handle_start_event(self, socket, player_id):
        socket.sendall(encode(self._get_start_message(player_id)))

        self._notify_other_sockets_except(
            socket,
            encode(Event.OTHER_PLAYER_JOINED + player_id))

    def _handle_player_action_events(self, socket, player_id, events):
        if events[3] == "exit":
            self._handle_exit_event(socket, player_id)
        else:
            self.players_position[player_id] = (events[1], events[2])

            message = Event.PLAYER + player_id + Event.DELIM + \
                    Event.ACTION + events[3] + Event.DELIM

            self._notify_other_sockets_except(
                socket,
                encode(message))

    def _handle_exit_event(self, socket, player_id):
        # send confirm to the exited client
        socket.sendall(encode(Event.EXIT))

        message_to_other_clients = Event.EXIT + str(player_id) + Event.DELIM
        self._notify_other_sockets_except(socket, encode(message_to_other_clients))

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

    def _get_start_message(self, player_id):
        message = Event.START

        connected_sockets_size = len(self.connected_sockets)
        message += (str(connected_sockets_size - 1) + Event.DELIM)

        for socket, id in self.connected_sockets:
            if id != player_id:
                message += (id + Event.DELIM)
                message += (str(self.players_position[id][0]) + Event.DELIM)
                message += (str(self.players_position[id][1]) + Event.DELIM)

        message += (player_id + Event.DELIM)

        return message

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
