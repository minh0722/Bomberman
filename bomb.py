import pygame
from object import Object
from game_settings import *
from arena import Arena
from pyganim import PygAnimation, PygConductor

class BombState:
    TICKING = 1
    EXPLODING = 2


class Bomb(Object):
    def __init__(self, position, bomb_range, arena):
        Object.__init__(self, position)

        self.range = bomb_range
        self.state = BombState.TICKING
        self.arena = arena
        
        self.bomb_sprite = self._create_bomb()
        self.explosion_center_sprite = self._create_center_explosion()
        self.explosion_left = self._create_left_explosion()
        self.explosion_right = self._create_right_explosion()
        self.explosion_up = self._create_up_explosion()
        self.explosion_down = self._create_down_explosion()
        self.explosion_left_end = self._create_left_end_explosion()
        self.explosion_right_end = self._create_right_end_explosion()
        self.explosion_up_end = self._create_up_end_explosion()
        self.explosion_down_end = self._create_down_end_explosion()

        self.tiles_can_explode_left = arena.tiles_can_be_exploded_to_the_left(self.normalize_position())
        self.tiles_can_explode_right = arena.tiles_can_be_exploded_to_the_right(self.normalize_position())
        self.tiles_can_explode_up = arena.tiles_can_be_exploded_to_the_up(self.normalize_position())
        self.tiles_can_explode_down = arena.tiles_can_be_exploded_to_the_down(self.normalize_position())

        self.bomb_sprite.play()

    def draw(self, game_display):
        if bomb_sprite.isFinished():
            self.set_state(BombState.EXPLODING)
        if self.state is BombState.TICKING:
            bomb_sprite.blit(game_display, self.position())
        elif self.state is BombState.EXPLODING:
            self._draw_bomb_left()

    def set_state(self, new_state):
        self.state = new_state
            
    def current_state(self):
        return self.state

    def _draw_bomb_left(self, game_display):
        if self.tiles_can_explode_left == 0:
            return None
        
        x = self.normalize_position()[0]
        y = self.normalize_position()[1]

        for explosion_x in range(x - 1, x - min(self.tiles_can_explode_left, self.range) - 1, -1):
            self.explosion_left.blit(
                game_display, 
                (explosion_x * TILE_SIZE, y * TILE_SIZE))

        self.explosion_left.play()

    def _draw_bomb_right(self, game_display):
        if self.tiles_can_explode_right == 0:
            return None

        x = self.normalize_position()[0]
        y = self.normalize_position()[1]

        for explosion_x in range(x + 1, x + min(self.tiles_can_explode_right, self.range) + 1):
            self.explosion_right.blit(
                game_display,
                (explosion_x * TILE_SIZE, y * TILE_SIZE))

        self.explosion_right.play()

    def _draw_bomb_up(self, game_display):
        if self.tiles_can_explode_up == 0:
            return None

        x = self.normalize_position()[0]
        y = self.normalize_position()[1]

        for explosion_y in range(y - 1, y - min(self.tiles_can_explode_up, self.range) - 1, -1):
            self.explosion_up.blit(
                game_display,
                (x * TILE_SIZE, explosion_y * TILE_SIZE))

        self.explosion_up.play()

    def _draw_bomb_down(self, game_display):
        if self.tiles_can_explode_down == 0:
            return None

        x = self.normalize_position()[0]
        y = self.normalize_position()[1]

        for explosion_y in range(y + 1, y + min(self.tiles_can_explode_down, self.range) + 1):
            self.explosion_down.blit(
                game_display,
                (x * TILE_SIZE, explosion_y * TILE_SIZE))

        self.explosion_down.play()

    def _create_bomb(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/normal_bomb_1.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_2.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_3.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_4.png", BOMB_FRAME_DURATION)
            ])

    def _create_center_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_center.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_center.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_center.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_center.png", EXPLOSION_DURATION)])

    def _create_left_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_left.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_left.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_left.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_left.png", EXPLOSION_DURATION)])

    def _create_right_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_right.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_right.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_right.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_right.png", EXPLOSION_DURATION)])

    def _create_up_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_up.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_up.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_up.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_up.png", EXPLOSION_DURATION)])

    def _create_down_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_down.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_down.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_down.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_down.png", EXPLOSION_DURATION)])

    def _create_left_end_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_left_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_left_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_left_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_left_end.png", EXPLOSION_DURATION)])

    def _create_right_end_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_right_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_right_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_right_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_right_end.png", EXPLOSION_DURATION)])

    def _create_up_end_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_up_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_up_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_up_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_up_end.png", EXPLOSION_DURATION)])

    def _create_down_end_explosion(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_down_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_down_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_1/explosion_down_end.png", EXPLOSION_DURATION),
            ("resources/battle_tiles/battle_stage_1/explosion_2/explosion_down_end.png", EXPLOSION_DURATION)])

# game_display = pygame.display.set_mode((765,675))
# a = Arena()
# b = Bomb((3,3), 2, a)