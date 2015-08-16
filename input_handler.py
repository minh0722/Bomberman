import pygame
from game_settings import *
from network_events import Event


class InputHandler:
    def __init__(self, player):
        self.player = player

    def handle_input(self):
        event = pygame.event.poll()

        if event.type == pygame.NOEVENT:
            pass

        if event.type == pygame.QUIT:
            return Event.EXIT

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
                return Event.PLACE_BOMB

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or
                    event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                self.player.pause_reset_sprite()
                return Event.RELEASED

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] and not keys[pygame.K_DOWN] and
                not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.player.move_up()
            return Event.MOVE_UP

        if (keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and
                not keys[pygame.K_LEFT] and not keys[pygame.K_DOWN]):
            self.player.move_right()
            return Event.MOVE_RIGHT

        if (keys[pygame.K_DOWN] and not keys[pygame.K_UP] and
                not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
            self.player.move_down()
            return  Event.MOVE_DOWN

        if (keys[pygame.K_LEFT] and not keys[pygame.K_UP] and
                not keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN]):
            self.player.move_left()
            return Event.MOVE_LEFT
