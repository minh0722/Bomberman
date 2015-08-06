from game_settings import *
from player import Direction


class Physics:
    def __init__(self, arena):
        self.arena = arena

    def resolve_player_collision(self, player, direction):
        if self._resolve_border_collision(player, direction):
            return None

        player_tile = player.get_player_tile()

        for wall in self.arena.get_non_destructible_walls():
            if player_tile.is_intersected_with(wall):
                self._resolve_wall_collision(player, wall, direction)
                break

        for wall in self.arena.get_destructible_walls():
            if player_tile.is_intersected_with(wall):
                self._resolve_wall_collision(player, wall, direction)
                break

    def _resolve_border_collision(self, player, direction):
        # returns True if border resolvement is done
        # else return False

        LAST_ROW_Y = 630
        LAST_COLUMN_X = 720

        player_tile = player.get_player_tile()

        x = player_tile.get_x()
        y = player_tile.get_y()

        border_resolvement_is_done = False

        if direction == Direction.UP:
            if y < 45:
                y = 45
                border_resolvement_is_done = True

        elif direction == Direction.DOWN:
            if y + TILE_HEIGHT > LAST_ROW_Y:
                y = LAST_ROW_Y - TILE_HEIGHT
                border_resolvement_is_done = True

        elif direction == Direction.LEFT:
            if x < 45:
                x = 45
                border_resolvement_is_done = True

        elif direction == Direction.RIGHT:
            if x + TILE_WIDTH > LAST_COLUMN_X:
                x = LAST_COLUMN_X - TILE_WIDTH
                border_resolvement_is_done = True

        player.set_player_tile_position((x, y))

        return border_resolvement_is_done

    def _resolve_wall_collision(self, player, wall, direction):
        player_tile = player.get_player_tile()

        x = player_tile.get_x()
        y = player_tile.get_y()

        if direction == Direction.UP:
            if self._player_is_left_to_wall(player_tile, wall):
                player.move_left()

            elif self._player_is_right_to_wall(player_tile, wall):
                player.move_right()

            else:
                player.set_player_tile_position(
                    (x, wall.get_y() + wall.get_height()))

        elif direction == Direction.DOWN:
            if self._player_is_left_to_wall(player_tile, wall):
                player.move_left()

            elif self._player_is_right_to_wall(player_tile, wall):
                player.move_right()

            else:
                player.set_player_tile_position(
                    (x, wall.get_y() - TILE_HEIGHT))

        elif direction == Direction.LEFT:
            if self._player_is_up_to_wall(player_tile, wall):
                player.move_up()

            elif self._player_is_down_to_wall(player_tile, wall):
                player.move_down()

            else:
                player.set_player_tile_position(
                    (wall.get_x() + wall.get_width(), y))

        elif direction == Direction.RIGHT:
            if self._player_is_up_to_wall(player_tile, wall):
                player.move_up()

            elif self._player_is_down_to_wall(player_tile, wall):
                player.move_down()

            else:
                player.set_player_tile_position(
                    (wall.get_x() - wall.get_width(), y))

    def _player_is_left_to_wall(self, player_tile, wall):
        return player_tile.get_x() <= wall.get_x() - 10

    def _player_is_right_to_wall(self, player_tile, wall):
        return player_tile.get_x() >= wall.get_x() + 10

    def _player_is_up_to_wall(self, player_tile, wall):
        return player_tile.get_y() <= wall.get_y() - 10

    def _player_is_down_to_wall(self, player_tile, wall):
        return player_tile.get_y() >= wall.get_y() + 10
