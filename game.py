import pygame
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

    def run(self):
        pygame.display.update()
        self.clock.tick(FPS)


class OnlineGame(Game):
    def __init__(self, game_display):
        Game.__init__(self, game_display)
        self.client = Client(game_display)

    def run(self):
        if self.client.connected() is False:
            pygame.quit()
            quit()

        self.client.run()
        Game.run(self)

    def send_player_action(self, player_action):
        if player_action is not None:
            self.client.send_packet(encode(player_action))

            if player_action == Event.EXIT:
                pygame.quit()
                quit()


class OfflineGame(Game):
    def __init__(self, game_display):
        Game.__init__(self, game_display)

    def run(self):
        Game.run(self)