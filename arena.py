import pygame
from drawable import Drawable
from util import *
from game_settings import *
from pyganim import *
from object import Object
from bomb import Bomb, BombState

# 0 - grass
# 1 - non destructible wall
# 2 - bomb
# 3 - destructible wall
# 4 - border

class TileType:
    GRASS = 0
    NON_DESTRUCTIBLE = 1
    BOMB = 2
    DESTRUCTIBLE = 3
    BORDER = 4


class Arena(Drawable):
    def __init__(self):
        Drawable.__init__(self)
        self.arena_matrix = [
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]

        self.arena_surface = self._load_arena_surface()
        self.bombs = list()

    def draw(self, game_display):
        game_display.blit(self.arena_surface, (0, 0))

        for bomb in self.bombs:
            if bomb.current_state() == BombState.EXPLODED:
                self.bombs.remove(bomb)
            else:
                bomb.draw(game_display)

    def place_bomb(self, position):
        correct_position = Object.get_normalized_position(position)

        b = Bomb((correct_position[1] * TILE_SIZE, correct_position[0] * TILE_SIZE), 5, self)
        self.bombs.append(b)

    def tiles_can_be_exploded_to_the_left(self, normalized_position):
        x = normalized_position[0]
        y = normalized_position[1]

        if (y - 1 < 0 or self.arena_matrix[x][y - 1] == TileType.BORDER or
                self.arena_matrix[x][y - 1] == TileType.NON_DESTRUCTIBLE):
            return 0

        for destructible_wall_index in range(y - 1, 0, -1):
            if self.arena_matrix[x][destructible_wall_index] == TileType.DESTRUCTIBLE:
                return y - destructible_wall_index
        return y - 1
        
        # TODO: need to check if it's bomb?

    def tiles_can_be_exploded_to_the_right(self, normalized_position):
        x = normalized_position[0]
        y = normalized_position[1]

        if (y + 1 >= ARENA_WIDTH or self.arena_matrix[x][y + 1] == TileType.BORDER or
                self.arena_matrix[x][y + 1] == TileType.NON_DESTRUCTIBLE):
            return 0

        for destructible_wall_index in range(y + 1, ARENA_WIDTH):
            if self.arena_matrix[x][destructible_wall_index] == TileType.DESTRUCTIBLE:
                return destructible_wall_index - y
        return ARENA_WIDTH - 2 - y

    def tiles_can_be_exploded_to_the_up(self, normalized_position):
        x = normalized_position[0]
        y = normalized_position[1]

        if (x - 1 < 0 or self.arena_matrix[x - 1][y] == TileType.BORDER or
                self.arena_matrix[x - 1][y] == TileType.NON_DESTRUCTIBLE):
            return 0

        for destructible_wall_index in range(x - 1, 0, -1):
            if self.arena_matrix[destructible_wall_index][y] == TileType.DESTRUCTIBLE:
                return x - destructible_wall_index
        return x - 1

    def tiles_can_be_exploded_to_the_down(self, normalized_position):
        x = normalized_position[0]
        y = normalized_position[1]

        if (x + 1 >= ARENA_HEIGHT or self.arena_matrix[x + 1][y] == TileType.BORDER or
                self.arena_matrix[x + 1][y] == TileType.NON_DESTRUCTIBLE):
            return 0
        
        for destructible_wall_index in range(x + 1, ARENA_HEIGHT):
            if self.arena_matrix[destructible_wall_index][y] == TileType.DESTRUCTIBLE:
                return destructible_wall_index - x
        return ARENA_HEIGHT - 2 - x

    def _can_place_bomb(self, x, y):
        return self.arena_matrix[x][y] == 0

    def _load_arena_surface(self):
        arena = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        for x in range(0, ARENA_HEIGHT):
            for y in range(0, ARENA_WIDTH):
                if self.arena_matrix[x][y] == 0:
                    arena.blit(
                        self._create_tile('grass'),
                        (y * TILE_SIZE, x * TILE_SIZE))
                elif self.arena_matrix[x][y] == 1:
                    arena.blit(
                        self._create_tile('non_destructible'),
                        (y * TILE_SIZE, x * TILE_SIZE))
                elif self.arena_matrix[x][y] == 4:
                    arena.blit(
                        self._create_tile('border'),
                        (y * TILE_SIZE, x * TILE_SIZE))
        return arena

    def _create_tile(self, type):
        if type is 'grass':
            return load_image('battle_tiles/battle_stage_1/grass_tile.png').convert()
        elif type is 'destructible':
            return load_image('battle_tiles/battle_stage_1/destructible_tile.png').convert()
        elif type is 'non_destructible':
            return load_image('battle_tiles/battle_stage_1/non_destructible_tile.png').convert()
        elif type is 'border':
            return load_image('battle_tiles/battle_stage_1/border_tile.png').convert()

    def _create_bomb(self):
        return PygAnimation([
            ("resources/battle_tiles/battle_stage_1/normal_bomb_1.png", 0.25),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_2.png", 0.25),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_3.png", 0.25),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_4.png", 0.25)
            ])
