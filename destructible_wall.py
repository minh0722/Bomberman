import pygame
from object import Object
from pyganim import PygAnimation, PygConductor
from util import *


class WallState:
    INTACT = 1
    DESTROYING = 2
    DESTROYED = 3

class DestructibleWall(Object):
    def __init__(self, position):
        Object.__init__(self, position, TILE_WIDTH, TILE_HEIGHT)

        self.state = WallState.INTACT
        self.destroying_wall_sprites = self._create_destroying_wall_sprites()
        self.intact_wall_image = self._create_wall_image()


    def draw(self, game_display):        
        if self.state == WallState.DESTROYED:
            return None

        elif self.state == WallState.INTACT:
            game_display.blit(self.intact_wall_image, self.position())

        elif self.state == WallState.DESTROYING:
            self.destroying_wall_sprites.blit(game_display, self.position())
            self.destroying_wall_sprites.play()

            if self.destroying_wall_sprites.isFinished():
                self.state = WallState.DESTROYED

    def _create_destroying_wall_sprites(self):
        return PygAnimation([
            (TILE_RESOURCE_PATH + "tile_destroyed_1.png", WALL_DESTROYED_FRAME_DURATION),
            (TILE_RESOURCE_PATH + "tile_destroyed_2.png", WALL_DESTROYED_FRAME_DURATION),
            (TILE_RESOURCE_PATH + "tile_destroyed_3.png", WALL_DESTROYED_FRAME_DURATION),
            (TILE_RESOURCE_PATH + "tile_destroyed_4.png", WALL_DESTROYED_FRAME_DURATION),
            (TILE_RESOURCE_PATH + "tile_destroyed_5.png", WALL_DESTROYED_FRAME_DURATION),
            (TILE_RESOURCE_PATH + "tile_destroyed_6.png", WALL_DESTROYED_FRAME_DURATION)],
            loop=False)

    def _create_wall_image(self):
        return load_image(
                TILE_RESOURCE_PATH +  "destructible_tile.png").convert()
