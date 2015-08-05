import pygame
from pyganim import PygAnimation, PygConductor
from pygame.sprite import Sprite
from object import Object
from game_settings import *
from bomb import Bomb, BombState


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
        Object.__init__(
            self,
            position,
            PLAYER_RECTANGLE_WIDTH,
            PLAYER_RECTANGLE_HEIGHT)

        self.bomb_capacity = 2
        self.placed_bomb = 0
        self.bomb_range = 3
        self.movement_speed = 3
        self.current_face_direction = Direction.DOWN
        self.state = PlayerState.ALIVE
        self.arena = arena

        self.player_down_sprite = self._create_player_down()
        self.player_up_sprite = self._create_player_up()
        self.player_left_sprite = self._create_player_left()
        self.player_right_sprite = self._create_player_right()

        self.player_die_sprite = self._create_player_die()

        self.sprite_conductor = PygConductor(
            self.player_down_sprite,
            self.player_up_sprite,
            self.player_left_sprite,
            self.player_right_sprite)

        self.sprite_conductor.pause()

        self.bombs = list()

        self.tile_position = Object(
            (45, 45),
            PLAYER_RECTANGLE_WIDTH,
            PLAYER_RECTANGLE_WIDTH)

    def move_up(self):
        Object.move_up(self, self.movement_speed)
        self.tile_position.move_up(self.movement_speed)

        resolved_tile_position = self.arena.physics.resolve_player_collision(
            self.tile_position,
            Direction.UP)

        self.tile_position.set_position(resolved_tile_position)
        self.set_y(resolved_tile_position[1] - TILE_OFFSET_Y)

        self.current_face_direction = Direction.UP
        self.player_up_sprite.play()

    def move_down(self):
        Object.move_down(self, self.movement_speed)
        self.tile_position.move_down(self.movement_speed)

        resolved_tile_position = self.arena.physics.resolve_player_collision(
            self.tile_position,
            Direction.DOWN)

        self.tile_position.set_position(resolved_tile_position)
        self.set_y(resolved_tile_position[1] - TILE_OFFSET_Y)

        self.current_face_direction = Direction.DOWN
        self.player_down_sprite.play()

    def move_left(self):
        Object.move_left(self, self.movement_speed)
        self.tile_position.move_left(self.movement_speed)

        resolved_tile_position = self.arena.physics.resolve_player_collision(
            self.tile_position,
            Direction.LEFT)

        self.tile_position.set_position(resolved_tile_position)
        self.set_x(resolved_tile_position[0] - TILE_OFFSET_X)

        self.current_face_direction = Direction.LEFT
        self.player_left_sprite.play()

    def move_right(self):
        Object.move_right(self, self.movement_speed)
        self.tile_position.move_right(self.movement_speed)

        resolved_tile_position = self.arena.physics.resolve_player_collision(
            self.tile_position,
            Direction.RIGHT)

        self.tile_position.set_position(resolved_tile_position)
        self.set_x(resolved_tile_position[0] - TILE_OFFSET_X)

        self.current_face_direction = Direction.RIGHT
        self.player_right_sprite.play()

    def is_alive(self):
        return self.state is PlayerState.ALIVE

    def die(self):
        self.state = PlayerState.DYING
        self.player_die_sprite.play()

    def place_bomb(self):
        if self.placed_bomb < self.bomb_capacity:
            normalized_position = Object.get_normalized_position(self.position())

            correct_position = (
                normalized_position[1] * TILE_SIZE,
                normalized_position[0] * TILE_SIZE)

            self.bombs.append(Bomb(correct_position, self.bomb_range, self.arena))
            self.placed_bomb += 1

    def pause_reset_sprite(self):
        self.sprite_conductor.pause_reset()

    def draw(self, game_display):
        self._draw_bombs(game_display)
        self._draw_player(game_display)

        print("Position: ", self.position())
        print("tile_position: ",self.tile_position.position())

    def _draw_bombs(self, game_display):
        for bomb in self.bombs:
            self.arena.update_explosion_in_matrix(bomb)

            if bomb.current_state() == BombState.EXPLODED:
                self.bombs.remove(bomb)
                self.placed_bomb -= 1

            bomb.draw(game_display)

    def _draw_player(self, game_display):
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
