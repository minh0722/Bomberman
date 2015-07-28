class Command:
	def __init__(self):
		pass

	def execute(self, player):
		pass

class PlaceBomb(Command):
	def __init__(self):
		Command.__init__(self)

	def execute(self, player):
		player.place_bomb()


class TriggerBomb(Command):
	def __init__(self):
		Command.__init__(self)

	def execute(self, player):
		player.trigger_bomb()

class MoveCommand:
	def __init__(self):
		pass

	def execute(self, player, direction):
		if direction is "up":
			player.move_up()
		elif direction is "down":
			player.move_down()
		elif direction is "left":
			player.move_left()
		elif direction is "right":
			player.move_right()

