from game_settings import *

class Physics:
	def __init__(self):
		self.x_limits = (LEFT_BORDER_X, RIGHT_BORDER_X)
		self.y_limits = (UP_BORDER_Y, DOWN_BORDER_Y)

		self.column_x = list()
		self.row_y = list()

		for col in range(0,8):
			self.column_x.append(LEFT_BORDER_X + col * CELL_WIDTH)

		for row in range(0,7):
			self.row_y.append(0 + row * CELL_WIDTH)

		self.corner_x = list()
		self.corner_y = list()

		for col in range(0, 8):
			left_corner = 58 + CELL_WIDTH * col
			right_corner = left_corner + 21
			self.corner_x.append((left_corner,right_corner))

		for row in range(0, 7):
			up_corner = 33 + CELL_WIDTH * row
			down_corner = up_corner + 21
			self.corner_y.append((up_corner, down_corner))

	def resolve_player_collision(self, x, y, direction):
		if x in self.column_x and y in self.row_y:
			return x, y
		if direction is "up":
			if y in self.row_y:
				return x, y
			y = max(y, self.y_limits[0])
			if x not in self.column_x:
				y = self.row_y[y // CELL_WIDTH + 1]
		
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
				y = self.row_y[y // CELL_WIDTH]
		
		if direction is "left":
			if x in self.column_x:
				return x, y
			x = max(x, self.x_limits[0])
			if y not in self.row_y:
				x = self.column_x[(x - LEFT_BORDER_X) // CELL_WIDTH + 1]

		return x, y