from game_settings import *
from player import Direction


class Physics:
    def __init__(self, arena):
        self.arena = arena

    def resolve_player_collision(self, player_tile, direction):
        x = player_tile.get_x()
        y = player_tile.get_y()

        resolved_border_position = \
            self._resolve_border_collision(x, y, direction)

        if resolved_border_position != (-1, -1):
            return resolved_border_position

        for wall in self.arena.non_destructible_walls:
            if player_tile.is_intersected_with(wall):
                return self._resolve_wall_collision(
                    player_tile,
                    wall,
                    direction)

        return player_tile.position()

    def _resolve_border_collision(self, x, y, direction):
        LAST_ROW_Y = 630
        LAST_COLUMN_X = 720

        if direction == Direction.UP:
            if y < 45:
                y = 45
                return (x, y)

        elif direction == Direction.DOWN:
            if y + TILE_SIZE > LAST_ROW_Y:
                y = LAST_ROW_Y - TILE_SIZE
                return (x, y)

        elif direction == Direction.LEFT:
            if x < 45:
                x = 45
                return (x, y)

        elif direction == Direction.RIGHT:
            if x + TILE_SIZE > LAST_COLUMN_X:
                x = LAST_COLUMN_X - TILE_SIZE
                return (x, y)

        return (-1, -1)

    def _resolve_wall_collision(self, player_tile, wall, direction):
        x = player_tile.get_x()
        y = player_tile.get_y()

        if direction == Direction.UP:
            y = wall.get_y() + wall.get_height()
            print("_player_is_left_to_wall: ", self._player_is_left_to_wall(player_tile, wall))
            print("_player_is_right_to_wall: ", self._player_is_right_to_wall(player_tile, wall))

        elif direction == Direction.DOWN:
            y = wall.get_y() - TILE_SIZE
            print("_player_is_left_to_wall: ", self._player_is_left_to_wall(player_tile, wall))
            print("_player_is_right_to_wall: ", self._player_is_right_to_wall(player_tile, wall))

        elif direction == Direction.LEFT:
            x = wall.get_x() + wall.get_width()
            print("_player_is_up_to_wall: ", self._player_is_up_to_wall(player_tile, wall))
            print("_player_is_down_to_wall: ", self._player_is_down_to_wall(player_tile, wall))

        elif direction == Direction.RIGHT:
            x = wall.get_x() - wall.get_width()
            print("_player_is_up_to_wall: ", self._player_is_up_to_wall(player_tile, wall))
            print("_player_is_down_to_wall: ", self._player_is_down_to_wall(player_tile, wall))

        return (x, y)

    def _can_slide_wall(self, player_tile, wall, direction):


        if direction == Direction.UP:
            pass

        elif direction == Direction.DOWN:
            pass

        elif direction == Direction.LEFT:
            pass

        elif direction == Direction.RIGHT:
            pass

    def _player_is_left_to_wall(self, player_tile, wall):
        return player_tile.get_x() <= wall.get_x() - 25

    def _player_is_right_to_wall(self, player_tile, wall):
        return player_tile.get_x() >= wall.get_x() + 20

    def _player_is_up_to_wall(self, player_tile, wall):
        return player_tile.get_y() <= wall.get_y() - 18

    def _player_is_down_to_wall(self, player_tile, wall):
        return player_tile.get_y() >= wall.get_y() + 10