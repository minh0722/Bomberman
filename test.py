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
pygame.display.set_caption('Bomberman')

pygame.display.update()

gameExit = False

clock = pygame.time.Clock()

x_move = 0
y_move = 0

x_change = 0
y_change = 0

frame_duration = 0.2
player_down = PygAnimation([
    ("resources/characters/bbm_front1.png", frame_duration),
    ("resources/characters/bbm_front2.png", frame_duration),
    ("resources/characters/bbm_front1.png", frame_duration),
    ("resources/characters/bbm_front3.png", frame_duration)
    ])
player_up = PygAnimation([
    ("resources/characters/bbm_back1.png", frame_duration),
    ("resources/characters/bbm_back2.png", frame_duration),
    ("resources/characters/bbm_back1.png", frame_duration),
    ("resources/characters/bbm_back3.png", frame_duration),
    ])
player_left = PygAnimation([
    ("resources/characters/bbm_left1.png", frame_duration),
    ("resources/characters/bbm_left2.png", frame_duration),
    ("resources/characters/bbm_left1.png", frame_duration),
    ("resources/characters/bbm_left3.png", frame_duration),
    ])
player_right = PygAnimation([
    ("resources/characters/bbm_right1.png", frame_duration),
    ("resources/characters/bbm_right2.png", frame_duration),
    ("resources/characters/bbm_right1.png", frame_duration),
    ("resources/characters/bbm_right3.png", frame_duration),
    ])

conductor = PygConductor(player_down, player_up, player_left, player_right)

# initially animation are in stopped state so nothing will be drawn
# so we call pause so it will be drawn
conductor.pause()

current_direction = "down"

p = Physics()

arena = Arena()
p1 = Player(22, 0)
input_handler = InputHandler(p1)

while not gameExit:
    arena.draw(game_display)
    p1.draw(game_display)

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         gameExit = True

    input_handler.handle_input()

    pygame.display.update()

    sec = clock.tick(FPS)


pygame.quit()
quit()