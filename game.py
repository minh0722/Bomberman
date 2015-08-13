import pygame
from arena import Arena
from player import Player
from input_handler import InputHandler
from pygame import Surface
from pygame.sprite import Sprite
from game_settings import *
from client import Client
from network_events import Event
from util import encode, decode


class Game:
    def __init__(self, game_display):
        self.game_display = game_display
        self.clock = pygame.time.Clock()

        self.arena = Arena()
        self.first_player = Player((22, 0), self.arena)
        self.input_handler = InputHandler(self.first_player)

        # for index in range(MAX_PLAYERS):
        #     new_player = Player((22,0), self.arena)
        #     self.players.append(new_player)

        # for player in self.players:
        #     self.arena.add_player(player)

        # self.input_handler = InputHandler(self.players[0])

        self.arena.add_player(self.first_player)

        self.client = Client()

    def run(self):
        if self.client.connected() is False:
            pygame.quit()
            quit()

        player_action = self.input_handler.handle_input()
    
        self.send_player_action(player_action)

        if not self.first_player.is_alive():
            self.send_player_action(Event.DIE)

        self.arena.draw(self.game_display)

        pygame.display.update()
        self.clock.tick(FPS)

    def send_player_action(self, player_action):
        if player_action is not None:
            self.client.send_packet(encode(player_action))

            if player_action == Event.EXIT:
                pygame.quit()
                quit()
