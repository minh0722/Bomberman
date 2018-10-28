import pygame
from object import Object
from pyganim import PygAnimation, PygConductor
from util import *
from game_settings import *
from sprite_create import *



class WallState:
    INTACT = 1
    DESTROYING = 2
    DESTROYED = 3

class DestructibleWall(Object):
    def __init__(self, position):
        Object.__init__(self, position, TILE_WIDTH, TILE_HEIGHT)

        self.state = WallState.INTACT
        self.destroying_wall_sprites = create_destroying_wall_sprites()
        self.intact_wall_image = create_destructible_wall_image()


    def draw(self, game_display):
        if self.state == WallState.DESTROYING:
            if self.destroying_wall_sprites.isFinished():
                self.state = WallState.DESTROYED

            self.destroying_wall_sprites.blit(game_display, self.position())

        elif self.state == WallState.INTACT:
            game_display.blit(self.intact_wall_image, self.position())


    def destroy(self):
        self.state = WallState.DESTROYING
        self.destroying_wall_sprites.play()

    def current_state(self):
        return self.state

