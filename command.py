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