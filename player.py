import pygame
from pyganim import PygAnimation, PygConductor
from pygame.sprite import Sprite
from object import Object
from game_settings import *


class PlayerState:
    ALIVE = 1
    DYING = 2
    DEAD = 3


class Direction:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Player(Object):
    def __init__(self, position, arena):
        Object.__init__(self, position)

        self.bomb_capacity = 1
        self.placed_bomb = 0
        self.bomb_range = 6
        self.movement_speed = 3
        self.current_face_direction = Direction.DOWN
        self.state = PlayerState.ALIVE
        self.arena = arena

        self.player_down_sprite = self._create_player_down()
        self.player_up_sprite = self._create_player_up()
        self.player_left_sprite = self._create_player_left()
        self.player_right_sprite = self._create_player_right()

        self.sprite_conductor = PygConductor(
            self.player_down_sprite,
            self.player_up_sprite,
            self.player_left_sprite,
            self.player_right_sprite)

        self.sprite_conductor.pause()

        self.player_die_sprite = self._create_player_die()

    def move_up(self):
        Object.move_up(self, self.movement_speed)

        if self.get_y() <= UP_BORDER_Y:
            self.set_y(UP_BORDER_Y)

        self.current_face_direction = Direction.UP
        self.player_up_sprite.play()

    def move_down(self):
        Object.move_down(self, self.movement_speed)

        if self.get_y() >= DOWN_BORDER_Y:
            self.set_y(DOWN_BORDER_Y)

        self.current_face_direction = Direction.DOWN
        self.player_down_sprite.play()

    def move_left(self):
        Object.move_left(self, self.movement_speed)

        if self.get_x() <= LEFT_BORDER_X:
            self.set_x(LEFT_BORDER_X)

        self.current_face_direction = Direction.LEFT
        self.player_left_sprite.play()

    def move_right(self):
        Object.move_right(self, self.movement_speed)

        if self.get_x() >= RIGHT_BORDER_X:
            self.set_x(RIGHT_BORDER_X)

        self.current_face_direction = Direction.RIGHT
        self.player_right_sprite.play()

    def is_alive(self):
        return self.state is PlayerState.ALIVE

    def die(self):
        self.state = PlayerState.DYING
        self.player_die_sprite.play()

    def place_bomb(self):
        self.arena.place_bomb(self.position(), self.bomb_range)

    def pause_reset_sprite(self):
        self.sprite_conductor.pause_reset()

    def draw(self, game_display):
        print("Position: ", self.position())

        if self.state is PlayerState.DEAD:
            return None

        if self.state is PlayerState.DYING:
            if self.player_die_sprite.isFinished():
                self.state = PlayerState.DEAD
            self.player_die_sprite.blit(game_display, self.position())

        elif self.state is PlayerState.ALIVE:
            if self.current_face_direction is Direction.DOWN:
                self.player_down_sprite.blit(game_display, self.position())
            if self.current_face_direction is Direction.UP:
                self.player_up_sprite.blit(game_display, self.position())
            if self.current_face_direction is Direction.LEFT:
                self.player_left_sprite.blit(game_display, self.position())
            if self.current_face_direction is Direction.RIGHT:
                self.player_right_sprite.blit(game_display, self.position())

    def _create_player_down(self):
        return PygAnimation([
            ("resources/characters/bbm_front1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_front2.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_front1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_front3.png", PLAYER_FRAME_DURATION)
            ])

    def _create_player_up(self):
        return PygAnimation([
            ("resources/characters/bbm_back1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_back2.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_back1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_back3.png", PLAYER_FRAME_DURATION),
            ])

    def _create_player_left(self):
        return PygAnimation([
            ("resources/characters/bbm_left1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_left2.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_left1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_left3.png", PLAYER_FRAME_DURATION),
            ])

    def _create_player_right(self):
        return PygAnimation([
            ("resources/characters/bbm_right1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_right2.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_right1.png", PLAYER_FRAME_DURATION),
            ("resources/characters/bbm_right3.png", PLAYER_FRAME_DURATION),
            ])

    def _create_player_die(self):
        return PygAnimation([
            ("resources/characters/bbm_die1.png", PLAYER_DIE_FRAME_DURATION),
            ("resources/characters/bbm_die2.png", PLAYER_DIE_FRAME_DURATION),
            ("resources/characters/bbm_die3.png", PLAYER_DIE_FRAME_DURATION),
            ("resources/characters/bbm_die4.png", PLAYER_DIE_FRAME_DURATION)],
            loop=False)
