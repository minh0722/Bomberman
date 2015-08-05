from game_settings import *
from player import Direction

class Physics:
    def __init__(self, arena):
        self.arena = arena

    def resolve_player_collision(self, player_tile, direction):
        x = player_tile.get_x()
        y = player_tile.get_y()

        resolved_border_position = self._resolve_border_collision(x, y, direction)

        if resolved_border_position != (-1, -1):
            return resolved_border_position

        for wall in self.arena.non_destructible_walls:
            if player_tile.is_intersected_with(wall):

                if direction == Direction.UP:
                    if y <= wall.get_y() + wall.get_height():
                        y = wall.get_y() + wall.get_height()

                elif direction == Direction.DOWN:
                    if y + TILE_SIZE >= wall.get_y():
                        y = wall.get_y() - TILE_SIZE

                elif direction == Direction.LEFT:
                    if x <= wall.get_x() + wall.get_width():
                        x = wall.get_x() + wall.get_width()

                elif direction == Direction.RIGHT:
                    if x + TILE_SIZE >= wall.get_x():
                        x = wall.get_x() - wall.get_width()

        return (x, y)

    def _resolve_border_collision(self, x, y, direction):
        if direction == Direction.UP:
            if y < 45:
                y = 45
                return (x, y)

        elif direction == Direction.DOWN:
            if y + TILE_SIZE > 585:
                y = 585 - TILE_SIZE
                return (x, y)

        elif direction == Direction.LEFT:
            if x < 45:
                x = 45
                return (x, y)

        elif direction == Direction.RIGHT:
            if x + TILE_SIZE > 720:
                x = 720 - TILE_SIZE
                return (x, y)

        return (-1, -1)