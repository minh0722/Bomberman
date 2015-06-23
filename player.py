import pygame
from pyganim import PygAnimation
from pygame.sprite import Sprite


class Player(Sprite):
	def __init__(self, position, player_number=0):
		Sprite.__init__(self)

		self._current_position = (0,0)
		self._bomb_capacity = 1
		self._bomb_range = 2
		self._movement_speed = 1
		self._current_face_direction = DOWN
		self._state

		