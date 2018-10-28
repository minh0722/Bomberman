import pygame
from game_settings import *

class Game:
    def __init__(self, game_display):
        self.game_display = game_display
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.display.update()
        self.clock.tick(FPS)
