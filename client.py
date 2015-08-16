import pygame
from game_settings import *
from socket import *
from game_settings import *
from network_socket import NetworkSocket
from threading import Thread
from util import encode, decode, get_event_list
from network_events import *
from arena import Arena
from player import Player, Direction
from input_handler import InputHandler


class Client:
    def __init__(self, game_display):
        self.game_display = game_display
        self.socket = NetworkSocket()
        self.socket.connect((SERVER_IP_ADDRESS, PORT))

        self.is_connected = True

        self.socket.set_blocking(0)

        self.send_packet(encode(Event.START))

        self.arena = Arena()
        self.players = list()
        self.input_handler = None

        self.receive_thread = Thread()
        self.receive_thread.run = self._receive_packet_from_server
        self.receive_thread.start()

    def run(self):
        if self.input_handler is not None:
            player_action = self.input_handler.handle_input()

            self.send_player_action(player_action)

            if not self.players[0].is_alive():
                self.send_player_action(Event.DIE + str(self.players[0].id))

            self.arena.draw(self.game_display)

    def send_packet(self, packet):
        self.socket.send_all(packet)

    def connected(self):
        return self.is_connected

    def send_player_action(self, player_action):
        if player_action is not None:
            message = Event.ACTION + \
                        str(self.players[0].get_x()) + Event.DELIM + \
                        str(self.players[0].get_y()) + Event.DELIM + \
                        player_action + Event.DELIM

            try:
                self.send_packet(encode(message))
            except Exception as e:
                print(e)

            if player_action == Event.EXIT:
                pygame.quit()
                quit()

    def _receive_packet_from_server(self):
        while True:
            try:
                packet = self.socket.recv()
                # print(packet)
                events = get_event_list(decode(packet))
                print("event list: ", events)

                self._handle_events(events)

                if events[0] == "exit" and len(events) == 1:
                    break
                elif decode(packet) == Event.SERVER_FULL:
                    print("Server full! Try again later!")
                    self.is_connected = False
                    break

                self.is_connected = True

            except Exception as e:
                pass

    def _handle_events(self, events):
        if events[0] == "start":
            self._handle_start_event(events)
        elif events[0] == "player":
            self._handle_player_event(events)
        elif events[0] == "joined":
            self._handle_joined_player_event(events)
        elif events[0] == "exit" and len(events) == 2:
            print("handle other exit")
            self._handle_player_exit(events)

    def _handle_joined_player_event(self, events):
        id = int(events[1])
        try:
            new_player = Player((22, 0), self.arena, id)

            self.players.append(new_player)
            self.arena.add_player(new_player)
        except Exception as e:
            print(e)
        print("added new player")

    def _handle_start_event(self, events):
        event_index = 1
        current_players_count = int(events[event_index])

        event_index += 1

        if current_players_count > 0:
            for index in range(current_players_count):
                print("creating other player")
                id = int(events[event_index])
                x = int(events[event_index + 1])
                y = int(events[event_index + 2])
                event_index += 3
                new_player = Player((x, y), self.arena, id)
                # new_player.set_player_tile_position((x, y))

                self.players.append(new_player)
                self.arena.add_player(new_player)

        player_id = int(events[event_index])
        print("id = ", player_id)

        this_player = Player((22, 0), self.arena, player_id)
        self.arena.add_player(this_player)
        self.players.insert(0, this_player)
        self.input_handler = InputHandler(this_player)

        print("start event handled...")

    def _handle_player_event(self, events):
        actions_count = len(events) // 4

        for action_index in range(actions_count):
            player_id = int(events[action_index * 4 + 1])
            action = events[action_index * 4 + 3]

            for player in self.players:
                if player.id == player_id:
                    if action == "up":
                        player.move_up()
                    elif action == "left":
                        player.move_left()
                    elif action == "down":
                        player.move_down()
                    elif action == "right":
                        player.move_right()
                    elif action == "bomb":
                        player.place_bomb()
                    elif action == "released":
                        player.pause_reset_sprite()

                    break

    def _handle_player_exit(self, events):
        exited_player_id = int(events[1])

        for player in self.players:
            print(player.id)
            if player.id == exited_player_id:
                try:
                    self.players.remove(player)
                except Exception as e:
                    print(e)

        for player in self.arena.players:
            print(player.id)
            if player.id == exited_player_id:
                try:
                    self.arena.players.remove(player)
                except Exception as e:
                    print(e)

    def __del__(self):
        print("joining thread")
        self.receive_thread.join()
        self.socket.close_socket()
