import pygame
from pyganim import PygAnimation, PygConductor
from pygame.sprite import Sprite
from object import Object
from game_settings import *

class Player(Object):
    def __init__(self, position, player_id=0):
        Object.__init__(self, position)

        self.bomb_capacity = 1
        self.placed_bomb = 0
        self.bomb_range = 2
        self.movement_speed = 1
        self.current_face_direction = 'DOWN'
        self.state = 'ALIVE'

        self.player_down_sprite = PygAnimation([
            ("resources/characters/bbm_front1.png", PLAYER_PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_front2.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_front1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_front3.png", PLAYER_FRAME_DURATION)
            ])

        self.player_up_sprite = PygAnimation([
            ("resources/characters/bbm_back1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_back2.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_back1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_back3.png", PLAYER_FRAME_DURATION),
            ])

        self.player_left_sprite = PygAnimation([
            ("resources/characters/bbm_left1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_left2.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_left1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_left3.png", PLAYER_FRAME_DURATION),
            ])

        self.player_right_sprite = PygAnimation([
            ("resources/characters/bbm_right1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_right2.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_right1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_right3.png", PLAYER_FRAME_DURATION),
            ])

        self.sprite_conductor = PygConductor(self.player_down_sprite, self.player_up_sprite, self.player_left_sprite, self.player_right_sprite)

        self.sprite_conductor.pause()

        self.player_die_sprite = PygAnimation([
            ("resources/characters/bbm_die1.png", PLAYER_DIE_FRAME_DURATION),
            ("resources/characters/bbm_die2.png", PLAYER_DIE_FRAME_DURATION),
            ("resources/characters/bbm_die3.png", PLAYER_DIE_FRAME_DURATION),
            ("resources/characters/bbm_die4.png", PLAYER_DIE_FRAME_DURATION)], loop=False)

    def pause_reset_sprite(self):
        self.sprite_conductor.pause_reset()

    def draw(self, game_display):
        if self.state is 'DEAD':
            if player_die_sprite.isFinished():
                pass
            player_die_sprite.blit(game_display, self.position())
        elif self.state is 'ALIVE':
            if self.current_face_direction is 'DOWN':
                player_down_sprite.blit(game_display, self.position())
            if self.current_face_direction is 'UP':
                player_up_sprite.blit(game_display, self.position())
            if self.current_face_direction is 'LEFT':
                player_left_sprite.blit(game_display, self.position())
            if self.current_face_direction is 'RIGHT':
                player_right_sprite.blit(game_display, self.position())

    def die(self):
        self.state = 'DEAD'
        self.player_die_sprite.play()

    def place_bomb(self, arena):
        arena.place_bomb(self.position()[0], self.position()[1])

