from drawable import Drawable
from game_settings import *


class Object(Drawable):
    def __init__(self, position):
        Drawable.__init__(self)
        self.x = position[0]
        self.y = position[1]

    def get_x(self):
    	return self.x

    def get_y(self):
    	return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_xy(self, x, y):
        self.x = x
        self.y = y

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

        if self.x in range(LEFT_BORDER_X, 52) and self.y in range(0, Y_OFFSET):
            return (1, 1)

        elif self.x not in range(LEFT_BORDER_X, X_OFFSET) and self.y not in range(0, Y_OFFSET):
            return ((self.y - Y_OFFSET) // 45 + 2, (self.x - X_OFFSET) // 45 + 2)

        elif self.x in range(LEFT_BORDER_X, 52) and self.y not in range(0, Y_OFFSET):
            return ((self.y - Y_OFFSET) // 45 + 2 ,1)
            
        elif self.x not in range(LEFT_BORDER_X, X_OFFSET) and self.y in range(0, Y_OFFSET):
            return (1, (self.x - X_OFFSET) // 45 + 2)

    @staticmethod
    def get_normalized_position(position):
        return (position[1] // 45 + 1, (position[0] - LEFT_BORDER_X) // 45 + 1)