import pygame
from object import Object
from game_settings import *
from arena import Arena
from pyganim import PygAnimation, PygConductor

class Bomb(Object):
    def __init__(self, position, bomb_range, arena):
        Object.__init__(self, position)

        self.range = bomb_range
        self.state = 'TICKING'
        
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

    def draw(self, game_display):
        pass

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

game_display = pygame.display.set_mode((765,675))
a = Arena()
b = Bomb((1,2), 2, a)