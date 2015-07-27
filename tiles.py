from util import *
from game_settings import *
import pygame

def create_tile(type):
	if type is 'grass':
		return load_image('battle_tiles/battle_stage_1/grass_tile.png').convert()
	elif type is 'destructible':
		return load_image('battle_tiles/battle_stage_1/destructible_tile.png').convert()
	elif type is 'non_destructible':
		return load_image('battle_tiles/battle_stage_1/non_destructible_tile.png').convert()
	elif type is 'border':
		return load_image('battle_tiles/battle_stage_1/border_tile.png').convert()

def create_arena():
	arena = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
	for x in range(0, 17):
		for y in range(0, 15):
			if x == 0 or x == 16 or y == 0 or y == 14:
				arena.blit(create_tile('border'), (x * 45, y * 45))
			elif x % 2 == 0 and y % 2 == 0 and x != 0 and y != 0:
				arena.blit(create_tile('non_destructible'), (x * 45, y * 45))
			else:
				arena.blit(create_tile('grass'), (x * 45, y * 45))
	return arena

def create_player():
	return load_image('characters/bbm_front1.png').convert_alpha()


