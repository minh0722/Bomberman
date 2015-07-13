class Command:
	def __init__(self):
		pass

	def execute(self, actor):
		pass

class PlaceBomb(Command):
	def __init__(self):
		Command.__init__(self)

	def execute(self, actor):
		actor.place_bomb()


class TriggerBomb(Command):
	def __init__(self):
		Command.__init__(self)

	def execute(self, actor):
		actor.trigger_bomb()