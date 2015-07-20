class Physics:
	def __init__(self):
		self.x_limits = (22, 652)
		self.y_limits = (0, 545)

		for col in range(0,8):
			self.walkable_x.append(22 + col * 90)

		for row in range(0,7):
			self.walkable_y.append(0 + row * 90)



	def resolve_collision(self, x, y, direction, arena):
		pass