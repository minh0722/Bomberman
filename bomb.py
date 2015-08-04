import pygame
from object import Object
from game_settings import *
from pyganim import PygAnimation, PygConductor


class BombState:
    TICKING = 1
    EXPLODING = 2
    EXPLODED = 3


class Bomb(Object):
    def __init__(self, position, bomb_range, arena):
        Object.__init__(self, position)

        self.range = bomb_range
        self.state = BombState.TICKING
        self.arena = arena

        self.bomb_sprite = self._create_bomb()
        self.explosion_center = self._create_center_explosion()
        self.explosion_left = self._create_left_explosion()
        self.explosion_right = self._create_right_explosion()
        self.explosion_up = self._create_up_explosion()
        self.explosion_down = self._create_down_explosion()
        self.explosion_left_end = self._create_left_end_explosion()
        self.explosion_right_end = self._create_right_end_explosion()
        self.explosion_up_end = self._create_up_end_explosion()
        self.explosion_down_end = self._create_down_end_explosion()

        self.tiles_can_explode_left = arena.left_tiles_can_be_exploded(
                                                self.normalize_position())

        self.tiles_can_explode_right = arena.right_tiles_can_be_exploded(
                                                self.normalize_position())

        self.tiles_can_explode_up = arena.up_tiles_can_be_exploded(
                                                self.normalize_position())

        self.tiles_can_explode_down = arena.down_tiles_can_be_exploded(
                                                self.normalize_position())

        # print("CAN EXPLODE LEFT: ", self.tiles_can_explode_left)
        # print("CAN EXPLODE RIGHT: ", self.tiles_can_explode_right)
        # print("CAN EXPLODE UP: ", self.tiles_can_explode_up)
        # print("CAN EXPLODE DOWN: ", self.tiles_can_explode_down)

        self.bomb_sprite.play()
        self.ticking_timer = BOMB_TIMER
        self.explosion_duration = EXPLOSION_DURATION

    def draw(self, game_display):
        if self.ticking_timer > 0:
            self.ticking_timer = self.ticking_timer - 1
        else:
            self._set_state(BombState.EXPLODING)
            if self.explosion_duration > 0:
                self.explosion_duration = self.explosion_duration - 1
            else:
                self._set_state(BombState.EXPLODED)

        if self._explosion_finished():
            self._set_state(BombState.EXPLODED)
            return None
        if self.state is BombState.TICKING:
            self.bomb_sprite.blit(game_display, self.position())
        if self.state is BombState.EXPLODING:
            self._draw_explosions(game_display)
        if self._done_ticking():
            self._set_state(BombState.EXPLODING)

    def current_state(self):
        return self.state

    def get_range(self):
        return self.range

    def _set_state(self, new_state):
        self.state = new_state

    def _done_ticking(self):
        return self.ticking_timer == 0

    def _explosion_finished(self):
        return self.explosion_duration == 0

    def _draw_explosions(self, game_display):
        self._draw_explosion_center(game_display)
        self._draw_explosion_left(game_display)
        self._draw_explosion_right(game_display)
        self._draw_explosion_up(game_display)
        self._draw_explosion_down(game_display)

    def _draw_explosion_center(self, game_display):
        x = self.normalize_position()[0]
        y = self.normalize_position()[1]

        self.explosion_center.blit(
            game_display,
            (y * TILE_SIZE, x * TILE_SIZE))

        self.explosion_center.play()

    def _draw_explosion_left(self, game_display):
        if self.tiles_can_explode_left == 0:
            return None

        x = self.normalize_position()[0]
        y = self.normalize_position()[1]

        max_explosion_index = y - min(self.tiles_can_explode_left, self.range) - 1

        for explosion_x in range(y - 1, max_explosion_index, -1):
            if explosion_x == max_explosion_index + 1:
                self.explosion_left_end.blit(
                    game_display,
                    (explosion_x * TILE_SIZE, x * TILE_SIZE))
            else:
                self.explosion_left.blit(
                    game_display,
                    (explosion_x * TILE_SIZE, x * TILE_SIZE))

        self.explosion_left.play()
        self.explosion_left_end.play()

    def _draw_explosion_right(self, game_display):
        if self.tiles_can_explode_right == 0:
            return None

        x = self.normalize_position()[0]
        y = self.normalize_position()[1]

        max_explosion_index = y + min(self.tiles_can_explode_right, self.range) + 1

        for explosion_x in range(y + 1, max_explosion_index):
            if explosion_x == max_explosion_index - 1:
                self.explosion_right_end.blit(
                    game_display,
                    (explosion_x * TILE_SIZE, x * TILE_SIZE))
            else:
                self.explosion_right.blit(
                    game_display,
                    (explosion_x * TILE_SIZE, x * TILE_SIZE))

        self.explosion_right.play()
        self.explosion_right_end.play()

    def _draw_explosion_up(self, game_display):
        if self.tiles_can_explode_up == 0:
            return None

        x = self.normalize_position()[0]
        y = self.normalize_position()[1]

        max_explosion_index = x - min(self.tiles_can_explode_up, self.range) - 1

        for explosion_y in range(x - 1, max_explosion_index, -1):
            if explosion_y == max_explosion_index + 1:
                self.explosion_up_end.blit(
                    game_display,
                    (y * TILE_SIZE, explosion_y * TILE_SIZE))
            else:
                self.explosion_up.blit(
                    game_display,
                    (y * TILE_SIZE, explosion_y * TILE_SIZE))

        self.explosion_up.play()
        self.explosion_up_end.play()

    def _draw_explosion_down(self, game_display):
        if self.tiles_can_explode_down == 0:
            return None

        x = self.normalize_position()[0]
        y = self.normalize_position()[1]

        max_explosion_index = x + min(self.tiles_can_explode_down, self.range) + 1

        for explosion_y in range(x + 1, max_explosion_index):
            if explosion_y == max_explosion_index - 1:
                self.explosion_down_end.blit(
                    game_display,
                    (y * TILE_SIZE, explosion_y * TILE_SIZE))
            else:
                self.explosion_down.blit(
                    game_display,
                    (y * TILE_SIZE, explosion_y * TILE_SIZE))

        self.explosion_down.play()
        self.explosion_down_end.play()

    def _create_bomb(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/normal_bomb_1.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_2.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_3.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_4.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_1.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_2.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_3.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_4.png", BOMB_FRAME_DURATION)],
            loop=False)

    def _create_center_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_center.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_center.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_center.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_center.png", EXPLOSION_FRAME_DURATION)],
            loop=False)

    def _create_left_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_left.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_left.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_left.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_left.png", EXPLOSION_FRAME_DURATION)],
            loop=False)

    def _create_right_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_right.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_right.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_right.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_right.png", EXPLOSION_FRAME_DURATION)],
            loop=False)

    def _create_up_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_up.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_up.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_up.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_up.png", EXPLOSION_FRAME_DURATION)],
            loop=False)

    def _create_down_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_down.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_down.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_down.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_down.png", EXPLOSION_FRAME_DURATION)],
            loop=False)

    def _create_left_end_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_left_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_left_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_left_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_left_end.png", EXPLOSION_FRAME_DURATION)],
            loop=False)

    def _create_right_end_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_right_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_right_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_right_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_right_end.png", EXPLOSION_FRAME_DURATION)],
            loop=False)

    def _create_up_end_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_up_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_up_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_up_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_up_end.png", EXPLOSION_FRAME_DURATION)],
            loop=False)

    def _create_down_end_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_down_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_down_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_down_end.png", EXPLOSION_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_down_end.png", EXPLOSION_FRAME_DURATION)],
            loop=False)
