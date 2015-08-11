import pygame
from drawable import Drawable
from util import *
from game_settings import *
from pyganim import *
from object import Object
from bomb import Bomb, BombState
from physics import Physics
from destructible_wall import DestructibleWall, WallState


class TileType:
    GRASS = 0
    NON_DESTRUCTIBLE = 1
    BOMB = 2
    DESTRUCTIBLE = 3
    BORDER = 4
    FLAME = 5


class Arena(Drawable):
    def __init__(self):
        Drawable.__init__(self)
        self.arena_matrix = [
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [4, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 3, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 3, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 0, 1, 3, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]

        self.arena_surface = self._load_arena_surface()
        self.non_destructible_walls = self._load_non_destructible_walls()
        self.destructible_walls = self._load_destructible_walls()
        self.players = list()
        self.physics = Physics(self)

    # TODO: remove this method
    def print_arena(self):
        for row in range(0, len(self.arena_matrix)):
            print(self.arena_matrix[row])
        print("\n")

    def draw(self, game_display):
        game_display.blit(self.arena_surface, (0, 0))

        self._update_players_state()
        self._draw_players_and_walls(game_display)

    def get_non_destructible_walls(self):
        return self.non_destructible_walls

    def get_destructible_walls(self):
        return self.destructible_walls

    def get_arena(self):
        return self.arena_matrix

    def add_player(self, new_player):
        if len(self.players) >= MAX_PLAYERS:
            return None
        self.players.append(new_player)

    def update_explosion_in_matrix(self, bomb):
        if bomb.current_state() == BombState.TICKING:
            return None

        bomb_state = bomb.current_state()

        new_tile_type = (TileType.FLAME if bomb_state == BombState.EXPLODING
                         else TileType.GRASS)

        self._update_matrix_explosion_center(bomb, new_tile_type)
        self._update_matrix_explosion_left(bomb, new_tile_type)
        self._update_matrix_explosion_right(bomb, new_tile_type)
        self._update_matrix_explosion_up(bomb, new_tile_type)
        self._update_matrix_explosion_down(bomb, new_tile_type)

    def left_tiles_can_be_exploded(self, normalized_position):
        x = normalized_position[0]
        y = normalized_position[1]

        if (y - 1 < 0 or self.arena_matrix[x][y - 1] == TileType.BORDER or
                self.arena_matrix[x][y - 1] == TileType.NON_DESTRUCTIBLE):
            return 0

        for wall_index in range(y - 1, 0, -1):
            if (self.arena_matrix[x][wall_index] == TileType.DESTRUCTIBLE or
                    self.arena_matrix[x][wall_index] == TileType.FLAME):
                return y - wall_index
        return y - 1

    def right_tiles_can_be_exploded(self, normalized_position):
        x = normalized_position[0]
        y = normalized_position[1]

        if (y + 1 >= ARENA_WIDTH or
                self.arena_matrix[x][y + 1] == TileType.BORDER or
                self.arena_matrix[x][y + 1] == TileType.NON_DESTRUCTIBLE):
            return 0

        for wall_index in range(y + 1, ARENA_WIDTH):
            if self.arena_matrix[x][wall_index] == TileType.DESTRUCTIBLE:
                # print("wall at pos: ", x, wall_index)
                # print("can explode = ", wall_index - y)
                return wall_index - y
        return ARENA_WIDTH - 2 - y

    def up_tiles_can_be_exploded(self, normalized_position):
        x = normalized_position[0]
        y = normalized_position[1]

        if (x - 1 < 0 or self.arena_matrix[x - 1][y] == TileType.BORDER or
                self.arena_matrix[x - 1][y] == TileType.NON_DESTRUCTIBLE):
            return 0

        for wall_index in range(x - 1, 0, -1):
            if self.arena_matrix[wall_index][y] == TileType.DESTRUCTIBLE:
                return x - wall_index
        return x - 1

    def down_tiles_can_be_exploded(self, normalized_position):
        x = normalized_position[0]
        y = normalized_position[1]

        if (x + 1 >= ARENA_HEIGHT or
                self.arena_matrix[x + 1][y] == TileType.BORDER or
                self.arena_matrix[x + 1][y] == TileType.NON_DESTRUCTIBLE):
            return 0

        for wall_index in range(x + 1, ARENA_HEIGHT):
            if self.arena_matrix[wall_index][y] == TileType.DESTRUCTIBLE:
                return wall_index - x
        return ARENA_HEIGHT - 2 - x

    def _draw_players_and_walls(self, game_display):
        for player in self.players:
            player.draw_bombs(game_display)

        self._draw_destructible_walls(game_display)

        for player in self.players:
            player.draw_player(game_display)

    def _update_players_state(self):
        for player in self.players:
            x = player.normalize_position_for_explosion()[0]
            y = player.normalize_position_for_explosion()[1]

            if self.arena_matrix[x][y] == TileType.FLAME:
                player.die()

    def _draw_destructible_walls(self, game_display):
        for wall in self.destructible_walls:
            x = wall.normalize_position()[0]
            y = wall.normalize_position()[1]

            if wall.current_state() == WallState.DESTROYED:
                self.destructible_walls.remove(wall)
                continue

            elif self.arena_matrix[x][y] == TileType.FLAME:
                wall.destroy()

            wall.draw(game_display)

    def _can_place_bomb(self, x, y):
        return self.arena_matrix[x][y] == 0

    def _update_matrix_explosion_center(self, bomb, new_tile_type):
        normalized_x = bomb.normalize_position()[0]
        normalized_y = bomb.normalize_position()[1]

        self.arena_matrix[normalized_x][normalized_y] = new_tile_type

    def _update_matrix_explosion_left(self, bomb, new_tile_type):
        normalized_position = bomb.normalize_position()
        bomb_range = bomb.get_range()

        can_explode_left = min(bomb_range, bomb.tiles_can_explode_left)

        for row in range(0, can_explode_left):
            x = normalized_position[0]
            y = normalized_position[1] - row - 1
            self.arena_matrix[x][y] = new_tile_type

    def _update_matrix_explosion_right(self, bomb, new_tile_type):
        normalized_position = bomb.normalize_position()
        bomb_range = bomb.get_range()

        can_explode_right = min(bomb_range, bomb.tiles_can_explode_right)

        for row in range(0, can_explode_right):
            x = normalized_position[0]
            y = normalized_position[1] + row + 1
            self.arena_matrix[x][y] = new_tile_type

    def _update_matrix_explosion_up(self, bomb, new_tile_type):
        normalized_position = bomb.normalize_position()
        bomb_range = bomb.get_range()

        can_explode_up = min(bomb_range, bomb.tiles_can_explode_up)

        for col in range(0, can_explode_up):
            x = normalized_position[0] - col - 1
            y = normalized_position[1]
            self.arena_matrix[x][y] = new_tile_type

    def _update_matrix_explosion_down(self, bomb, new_tile_type):
        normalized_position = bomb.normalize_position()
        bomb_range = bomb.get_range()

        can_explode_down = min(bomb_range, bomb.tiles_can_explode_down)

        for col in range(0, can_explode_down):
            x = normalized_position[0] + col + 1
            y = normalized_position[1]
            self.arena_matrix[x][y] = new_tile_type

    def _load_arena_surface(self):
        arena = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

        for x in range(0, ARENA_HEIGHT):
            for y in range(0, ARENA_WIDTH):
                if (self.arena_matrix[x][y] == TileType.GRASS or
                    self.arena_matrix[x][y] == TileType.DESTRUCTIBLE):
                    arena.blit(
                        self._create_tile(TileType.GRASS),
                        (y * TILE_HEIGHT, x * TILE_WIDTH))

                elif self.arena_matrix[x][y] == TileType.NON_DESTRUCTIBLE:
                    arena.blit(
                        self._create_tile(TileType.NON_DESTRUCTIBLE),
                        (y * TILE_HEIGHT, x * TILE_WIDTH))

                elif self.arena_matrix[x][y] == TileType.BORDER:
                    arena.blit(
                        self._create_tile(TileType.BORDER),
                        (y * TILE_HEIGHT, x * TILE_WIDTH))

        return arena

    def _load_non_destructible_walls(self):
        walls = list()

        for row in range(0, ARENA_HEIGHT):
            for column in range(0, ARENA_HEIGHT):
                if self.arena_matrix[row][column] == TileType.NON_DESTRUCTIBLE:
                    wall = Object(
                        (column * TILE_HEIGHT, row * TILE_WIDTH),
                        TILE_WIDTH,
                        TILE_HEIGHT)

                    walls.append(wall)

        return walls

    def _load_destructible_walls(self):
        walls = list()

        for row in range(0, ARENA_HEIGHT):
            for column in range(0, ARENA_HEIGHT):
                if self.arena_matrix[row][column] == TileType.DESTRUCTIBLE:
                    wall = DestructibleWall(
                            (column * TILE_HEIGHT, row * TILE_WIDTH))

                    walls.append(wall)

        return walls

    def _create_tile(self, type):
        if type is TileType.GRASS:
            return load_image(
                "battle_tiles/battle_stage_1/grass_tile.png").convert()

        elif type is TileType.DESTRUCTIBLE:
            return load_image(
                "battle_tiles/battle_stage_1/destructible_tile.png").convert()

        elif type is TileType.NON_DESTRUCTIBLE:
            return load_image(
                "battle_tiles/battle_stage_1/non_destruct_tile.png").convert()

        elif type is TileType.BORDER:
            return load_image(
                "battle_tiles/battle_stage_1/border_tile.png").convert()
