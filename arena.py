import pygame
from util import Drawable

class Arena(Drawable):
	def __init__(self):
		Drawable.__init__(self)

	def draw(self, sprite):
		pass

	def place_bomb(self, position):
		pass

	def _can_place_bomb(self, position):
		pass
