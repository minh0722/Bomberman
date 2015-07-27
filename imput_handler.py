import pygame
from game_settings import *

class InputHandler:
    def __init__(self, player):
        self.player = player
        self.x_pos = 0
        self.y_pos = 0
        self.x_change = 0
        self.y_change = 0

    def handle_input(self, pygame_event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_left.nextFrame()
            if event.key == pygame.K_RIGHT:
                player_right.nextFrame()
            if event.key == pygame.K_UP:
                player_up.nextFrame()
            if event.key == pygame.K_DOWN:
                player_down.nextFrame()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.pause_reset()
            if event.key == pygame.K_RIGHT:
                player.pause_reset()
            if event.key == pygame.K_UP:
                player.pause_reset()
            if event.key == pygame.K_DOWN:
                player.pause_reset()
            self.x_change = 0
            self.y_change = 0

        if self.x_pos > RIGHT_BORDER_X: x_pos = RIGHT_BORDER_X
        if x_pos < LEFT_BORDER_X: x_pos = LEFT_BORDER_X
        if y_pos > DOWN_BORDER_Y: y_pos = DOWN_BORDER_Y
        if y_pos < UP_BORDER_Y: y_pos = UP_BORDER_Y
