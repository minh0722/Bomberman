from game_settings import *


class Physics:
    def __init__(self):
        self.x_limits = (LEFT_BORDER_X, RIGHT_BORDER_X)
        self.y_limits = (UP_BORDER_Y, DOWN_BORDER_Y)

        self.column_x = list()
        self.row_y = list()

        for col in range(0, 8):
            self.column_x.append(LEFT_BORDER_X + col * CELL_WIDTH)

        for row in range(0, 7):
            self.row_y.append(0 + row * CELL_WIDTH)

        self.corner_x = list()
        self.corner_y = list()

        for col in range(0, 7):
            left_corner = 43 + CELL_WIDTH * col
            right_corner = left_corner + 48
            self.corner_x.append((left_corner, right_corner))

        for row in range(0, 6):
            up_corner = 27 + CELL_WIDTH * row
            down_corner = up_corner + 33
            self.corner_y.append((up_corner, down_corner))

    def resolve_player_collision(self, x, y, direction):
        if direction is "up":
            if y in self.row_y:
                return x, y
            y = max(y, self.y_limits[0])
            # if x not in self.column_x:
            #   y = self.row_y[y // CELL_WIDTH + 1]
            x, y = self.__resolve_corner_slide(x, y, direction)

        if direction is "right":
            if x in self.column_x:
                return x, y
            x = min(x, self.x_limits[1])
            if y not in self.row_y:
                x = self.column_x[(x - LEFT_BORDER_X) // CELL_WIDTH]

        if direction is "down":
            if y in self.row_y:
                return x, y
            y = min(y, self.y_limits[1])
            if x not in self.column_x:
                y = self.row_y[(int)(y // CELL_WIDTH)]

        if direction is "left":
            if x in self.column_x:
                return x, y
            x = max(x, self.x_limits[0])
            if y not in self.row_y:
                x = self.column_x[(x - LEFT_BORDER_X) // CELL_WIDTH + 1]

        return x, y

    def __resolve_corner_slide(self, x, y, direction):
        if self.__is_in_corner(x, y):
            if direction is "up":
                return x - 2, y - 0.01

    def __is_in_corner(self, x, y):
        for x_corner in self.corner_x:
            if x < x_corner[0] or x > x_corner[1]:
                return True

        for y_corner in self.corner_y:
            if y < y_corner[0] or y > y_corner[1]:
                return True

        return False

    def __is_in_corner_left(self, x, y):
        for x_corner in self.corner_x:
            if x < x_corner[0]:
                return True

        for y_corner in self.corner_y:
            if y < y_corner[0]:
                return True

        return False

    def __is_in_corner_right(self, x):
        for x_index in range(0, len(self.corner_x)):
            if x >= self.corner_x[x_index][1] and x < self.column_x[x_index + 1]:
                return True

        return False

    def __is_in_corner_left(self, x):
        for x_index in range(0, len(self.corner_x)):
            if x <= self.corner_x[x_index][0] and x > self.column_x[x_index]:
                return True

        return False
