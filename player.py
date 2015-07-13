import pygame
from pyganim import PygAnimation
from pygame.sprite import Sprite
from util import Drawable
from object import Object

class Player(Drawable, Object):
	def __init__(self, position, player_id=0):
		Drawable.__init__(self)
		Object.__init__(self, position)

		self._bomb_capacity = 1
		self._bomb_range = 2
		self._movement_speed = 1
		self._current_face_direction = 'DOWN'
		self._state = 'ALIVE'

	def draw(self, sprite):
		pass

	def die(self):
		pass

	def place_bomb(self, bomb_position):
		pass