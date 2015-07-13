from object import Object

class Actor(object):
	def __init__(self, x, y):
		object.__init__(self, x, y)

	def place_bomb(self):
		pass

	def trigger_bomb(self):
		pass