import pygame
from util import *
from tiles import *
from pygame import Surface
from pygame.sprite import Sprite
from pyganim import *
from physics import Physics
from game_settings import *
from arena import Arena
from player import Player
from input_handler import InputHandler

pygame.init()

game_display = pygame.display.set_mode((765,675))
pygame.display.set_caption('BomberMin')

pygame.display.update()

gameExit = False

clock = pygame.time.Clock()

arena = Arena()
p1 = Player((22, 0), arena)
p2 = Player((112, 0), arena)
input_handler = InputHandler(p1)

arena.add_player(p1)
arena.add_player(p2)

while not gameExit:
    arena.draw(game_display)
    p1.draw(game_display)
    p2.draw(game_display)

    input_handler.handle_input()

    pygame.display.update()

    sec = clock.tick(FPS)


pygame.quit()
quit()
