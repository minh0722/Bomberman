from drawable import Drawable
from game_settings import *


class Object(Drawable):
    def __init__(self, position, width, height):
        Drawable.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.width = width
        self.height = height

    def is_intersected_with(self, _object):
        top_left = (_object.x, _object.y)
        bottom_right = (_object.x + _object.width, _object.y + _object.height)

        this_object_top_left = (self.x, self.y)
        this_object_bottom_right = (self.x + self.width, self.y + self.height)

        return this_object_bottom_right[1] > top_left[1] \
            and this_object_bottom_right[0] > top_left[0] \
            and this_object_top_left[1] < bottom_right[1] \
            and this_object_top_left[0] < bottom_right[0]

    def contains_point(self, point):
        return self.x <= point[0] and point[0] <= self.x + self.width \
                and self.y <= point[1] and point[1] <= self.y + self.height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_position(self, position):
        self.x = position[0]
        self.y = position[1]

    def move_up(self, y):
        self.y -= y

    def move_down(self, y):
        self.y += y

    def move_left(self, x):
        self.x -= x

    def move_right(self, x):
        self.x += x

    def position(self):
        return (self.x, self.y)

    def normalize_position(self):
        return (self.y // 45, (self.x - LEFT_BORDER_X) // 45 + 1)

    def normalize_position_for_explosion(self):
        X_OFFSET = 43
        Y_OFFSET = 24

        if self._in_first_column() and self._in_first_row():
            return (1, 1)

        elif not self._in_first_column() and not self._in_first_row():
            return ((self.y - Y_OFFSET) // 45 + 2,
                    (self.x - X_OFFSET) // 45 + 2)

        elif self._in_first_column() and not self._in_first_row():
            return ((self.y - Y_OFFSET) // 45 + 2, 1)

        elif not self._in_first_column() and self._in_first_row():
            return (1, (self.x - X_OFFSET) // 45 + 2)

    @staticmethod
    def get_normalized_position(position):
        return (position[1] // 45 + 1, (position[0] - LEFT_BORDER_X) // 45 + 1)

    def _in_first_column(self):
        return self.x in range(LEFT_BORDER_X, 52)

    def _in_first_row(self):
        return self.y in range(0, 24)
