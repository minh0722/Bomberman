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


	def resolve_player_collision(self, x, y, direction, arena):
		if direction is "up":
			pass
		elif direction is "right":
			pass
		elif direction is "down":
			pass
		elif direction is "left":
			pass
