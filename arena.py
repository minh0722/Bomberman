import pygame
from drawable import Drawable
from util import *
from game_settings import *
from pyganim import *
from object import Object
from bomb import Bomb, BombState

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
        self.players = list()

    def draw(self, game_display):
        game_display.blit(self.arena_surface, (0, 0))

        for bomb in self.bombs:
            self._update_explosion_in_matrix(bomb)

            if bomb.current_state() == BombState.EXPLODED:
                self.bombs.remove(bomb)
            
            bomb.draw(game_display)

        for player in self.players:
            if not player.is_alive():
                self.players.remove(player)
            else:
                x = player.normalize_position_for_explosion()[0]
                y = player.normalize_position_for_explosion()[1]

                print("Player explosion position: ", player.normalize_position_for_explosion()[0], 
                    " ", player.normalize_position_for_explosion()[1])

                if self.arena_matrix[x][y] == TileType.FLAME:
                    player.die()

        # for row in range(0, len(self.arena_matrix)):
        #     print(self.arena_matrix[row])
        # print("\n")

    def add_player(self, new_player):
        if len(self.players) >= MAX_PLAYERS:
            return None
        self.players.append(new_player)

    def place_bomb(self, position, bomb_range):
        normalized_position = Object.get_normalized_position(position)

        correct_position = (
            normalized_position[1] * TILE_SIZE,
            normalized_position[0] * TILE_SIZE)

        b = Bomb(correct_position, bomb_range, self)
        self.bombs.append(b)

    def _can_place_bomb(self, x, y):
        return self.arena_matrix[x][y] == 0

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

    def _update_explosion_in_matrix(self, bomb):
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

    def _update_matrix_explosion_center(self, bomb, new_tile_type):
        normalized_position = bomb.normalize_position()

        self.arena_matrix[normalized_position[0]][normalized_position[1]] = new_tile_type

    def _update_matrix_explosion_left(self, bomb, new_tile_type):
        normalized_position = bomb.normalize_position()
        bomb_range = bomb.get_range()

        can_explode_left = min(bomb_range,
            self.tiles_can_be_exploded_to_the_left(normalized_position))

        for row in range(0, can_explode_left):
            self.arena_matrix[normalized_position[0]][normalized_position[1] - row - 1] = new_tile_type

    def _update_matrix_explosion_right(self, bomb, new_tile_type):
        normalized_position = bomb.normalize_position()
        bomb_range = bomb.get_range()

        can_explode_right = min(bomb_range,
            self.tiles_can_be_exploded_to_the_right(normalized_position))

        for row in range(0, can_explode_right):
            self.arena_matrix[normalized_position[0]][normalized_position[1] + row  + 1] = new_tile_type

    def _update_matrix_explosion_up(self, bomb, new_tile_type):
        normalized_position = bomb.normalize_position()
        bomb_range = bomb.get_range()

        can_explode_up = min(bomb_range,
            self.tiles_can_be_exploded_to_the_up(normalized_position))

        for col in range(0, can_explode_up):
            self.arena_matrix[normalized_position[0] - col - 1][normalized_position[1]] = new_tile_type

    def _update_matrix_explosion_down(self, bomb, new_tile_type):
        normalized_position = bomb.normalize_position()
        bomb_range = bomb.get_range()

        can_explode_down = min(bomb_range,
            self.tiles_can_be_exploded_to_the_down(normalized_position))

        for col in range(0, can_explode_down):
            self.arena_matrix[normalized_position[0] + col + 1][normalized_position[1]] = new_tile_type

    def _load_arena_surface(self):
        arena = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        for x in range(0, ARENA_HEIGHT):
            for y in range(0, ARENA_WIDTH):
                if self.arena_matrix[x][y] == TileType.GRASS:
                    arena.blit(
                        self._create_tile('grass'),
                        (y * TILE_SIZE, x * TILE_SIZE))
                elif self.arena_matrix[x][y] == TileType.NON_DESTRUCTIBLE:
                    arena.blit(
                        self._create_tile('non_destructible'),
                        (y * TILE_SIZE, x * TILE_SIZE))
                elif self.arena_matrix[x][y] == TileType.BORDER:
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
