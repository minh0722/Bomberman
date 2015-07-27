import pygame
from drawable import Drawable
from util import *
from game_settings import *

# 0 - grass
# 1 - non destructible wall
# 2 - bomb
# 3 - destructible wall
# 4 - border

class Arena(Drawable):
	def __init__(self):
		Drawable.__init__(self)
		self.arena_surface_matrix = [
			[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
			[4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
			[4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
			[4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
			[4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
			[4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
			[4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
			[4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
			[4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
			[4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
			[4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
			[4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
			[4, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4],
			[4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
			[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]

		self.arena_surface = self._load_arena_surface()

	def draw(self, game_display):
		game_display.blit(self.arena_surface, (0,0))

	def place_bomb(self, x, y):
		if self._can_place_bomb(x, y):
			self.arena_surface_matrix[x][y] = 2
		self.arena_surface = self._load_arena_surface()


	def _can_place_bomb(self, x, y):
		return self.arena_surface_matrix[x][y] == 0

	def _load_arena_surface(self):
		arena = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
		for x in range(0, ARENA_WIDTH):
			for y in range(0, ARENA_HEIGHT):
				if self.arena_surface_matrix[y][x] == 0:
					arena.blit(self._create_tile('grass'), (x * TILE_SIZE, y * TILE_SIZE))
				elif self.arena_surface_matrix[y][x] == 1:
					arena.blit(self._create_tile('non_destructible'), (x * TILE_SIZE, y * TILE_SIZE))
				elif self.arena_surface_matrix[y][x] == 4:
					arena.blit(self._create_tile('border'), (x * TILE_SIZE, y * TILE_SIZE))
		return arena

	def _create_tile(self, type):
		if type is 'grass':
			return load_image('battle_tiles/battle_stage_1/grass_tile.png').convert()
		elif type is 'destructible':
			return load_image('battle_tiles/battle_stage_1/destructible_tile.png').convert()
		elif type is 'non_destructible':
			return load_image('battle_tiles/battle_stage_1/non_destructible_tile.png').convert()
		elif type is 'border':
			return load_image('battle_tiles/battle_stage_1/border_tile.png').convert()

