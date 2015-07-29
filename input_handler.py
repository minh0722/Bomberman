import pygame
from game_settings import *

class InputHandler:
    def __init__(self, player):
        self.player = player
        # self.x_pos = 0
        # self.y_pos = 0
        # self.x_change = 0
        # self.y_change = 0

    def handle_input(self):
        event = pygame.event.poll()

        # for event in pygame.event.get():
        #     print("event")

        if event.type == pygame.NOEVENT:
            pass

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if not self.player.is_alive():
            return None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.player_left_sprite.nextFrame()
            if event.key == pygame.K_RIGHT:
                self.player.player_right_sprite.nextFrame()
            if event.key == pygame.K_UP:
                self.player.player_up_sprite.nextFrame()
            if event.key == pygame.K_DOWN:
                self.player.player_down_sprite.nextFrame()
            if event.key == pygame.K_SPACE:
                self.player.place_bomb()

            #TODO: remove...
            if event.key == pygame.K_d:
                self.player.die()

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or
                    event.key == pygame.K_UP or event.key == pygame.K_DOWN):
               self.player.pause_reset_sprite()

        # if self.x_pos > RIGHT_BORDER_X: x_pos = RIGHT_BORDER_X
        # if x_pos < LEFT_BORDER_X: x_pos = LEFT_BORDER_X
        # if y_pos > DOWN_BORDER_Y: y_pos = DOWN_BORDER_Y
        # if y_pos < UP_BORDER_Y: y_pos = UP_BORDER_Y

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] and not keys[pygame.K_DOWN] and
                not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.player.move_up()
        if (keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and
                not keys[pygame.K_LEFT] and not keys[pygame.K_DOWN]):
            self.player.move_right()
        if (keys[pygame.K_DOWN] and not keys[pygame.K_UP] and
                not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
            self.player.move_down()
        if (keys[pygame.K_LEFT] and not keys[pygame.K_UP] and
                not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN]):
            self.player.move_left()
