import pygame
from pyganim import PygAnimation, PygConductor
from pygame.sprite import Sprite
from object import Object

class Player(Object):
	def __init__(self, position, player_id=0):
		Object.__init__(self, position)

		self.bomb_capacity = 1
		self.placed_bomb = 0
		self.bomb_range = 2
		self.movement_speed = 1
		self.current_face_direction = 'DOWN'
		self.state = 'ALIVE'

		self.player_down_sprite = PygAnimation([
		    ("resources/characters/bbm_front1.png", frame_duration),
		    ("resources/characters/bbm_front2.png", frame_duration),
		    ("resources/characters/bbm_front1.png", frame_duration),
		    ("resources/characters/bbm_front3.png", frame_duration)
		    ])

		self.player_up_sprite = PygAnimation([
		    ("resources/characters/bbm_back1.png", frame_duration),
		    ("resources/characters/bbm_back2.png", frame_duration),
		    ("resources/characters/bbm_back1.png", frame_duration),
		    ("resources/characters/bbm_back3.png", frame_duration),
		    ])

		self.player_left_sprite = PygAnimation([
		    ("resources/characters/bbm_left1.png", frame_duration),
		    ("resources/characters/bbm_left2.png", frame_duration),
		    ("resources/characters/bbm_left1.png", frame_duration),
		    ("resources/characters/bbm_left3.png", frame_duration),
		    ])

		self.player_right_sprite = PygAnimation([
		    ("resources/characters/bbm_right1.png", frame_duration),
		    ("resources/characters/bbm_right2.png", frame_duration),
		    ("resources/characters/bbm_right1.png", frame_duration),
		    ("resources/characters/bbm_right3.png", frame_duration),
		    ])

		self.sprite_conductor = PygConductor(self.player_down_sprite, self.player_up_sprite, self.player_left_sprite, self.player_right_sprite)

		self.sprite_conductor.pause()

	def pause_reset_sprite(self):
		self.sprite_conductor.pause_reset()

	def draw(self, game_display):
		pass

	def die(self):
		self.state = 'DEAD'

	def place_bomb(self, arena):
		arena.place_bomb(self.position()[0], self.position()[1])

