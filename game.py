import pygame
from arena import Arena
from player import Player
from input_handler import InputHandler
from pygame import Surface
from pygame.sprite import Sprite
from game_settings import *


class Game:
    def __init__(self, game_display):
        self.game_display = game_display
        self.clock = pygame.time.Clock()

        self.arena = Arena()
        self.first_player = Player((22, 0), self.arena)
        self.input_handler = InputHandler(self.first_player)

        self.arena.add_player(self.first_player)

    def run(self):
        if self.first_player.client_is_connected() is False:
            pygame.quit()
            quit()

        self.input_handler.handle_input()
        self.arena.draw(self.game_display)

        pygame.display.update()
        self.clock.tick(FPS)
