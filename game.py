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
        self.arena.draw(self.game_display)
        self.input_handler.handle_input()

        pygame.display.update()
        self.clock.tick(FPS)
