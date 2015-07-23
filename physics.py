class Physics:
	def __init__(self):
		self.x_limits = (22, 652)
		self.y_limits = (0, 540)

		self.column_x = list()
		self.row_y = list()

		for col in range(0,8):
			self.column_x.append(22 + col * 90)

		for row in range(0,7):
			self.row_y.append(0 + row * 90)

		self.corner_x = list()
		self.corner_y = list()

		for col in range(0, 8):
			left_corner = 58 + 90 * col
			right_corner = left_corner + 21
			self.corner_x.append((left_corner,right_corner))

		for row in range(0, 7):
			up_corner = 33 + 90 * row
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
				y = self.row_y[y // 90 + 1]
		
		if direction is "right":
			if x in self.column_x:
				return x, y
			x = min(x, self.x_limits[1])
			if y not in self.row_y:
				x = self.column_x[(x - 22) // 90]
		
		if direction is "down":
			if y in self.row_y:
				return x, y
			y = min(y, self.y_limits[1])
			if x not in self.column_x:
				y = self.row_y[y // 90]
		
		if direction is "left":
			if x in self.column_x:
				return x, y
			x = max(x, self.x_limits[0])
			if y not in self.row_y:
				x = self.column_x[(x - 22) // 90 + 1]

		return x, y