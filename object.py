from drawable import Drawable

class Object(Drawable):
	def __init__(self, x, y):
		Drawable.__init__(self)
		self.x = x
		self.y = y

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

