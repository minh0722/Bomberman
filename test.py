import pygame
from util import *
from tiles import *
from pygame import Surface
from pygame.sprite import Sprite
from pyganim import *

pygame.init()

gameDisplay = pygame.display.set_mode((765,675))
pygame.display.set_caption('Bomberman')

pygame.display.update()

gameExit = False

clock = pygame.time.Clock()

x_move = 0
y_move = 0

x_change = 0
y_change = 0

arena = create_arena()

frame_duration = 0.2
player_down = PygAnimation([
	("resources/characters/bbm_front1.png", frame_duration),
	("resources/characters/bbm_front2.png", frame_duration),
	("resources/characters/bbm_front1.png", frame_duration),
	("resources/characters/bbm_front3.png", frame_duration)
	])
player_up = PygAnimation([
	("resources/characters/bbm_back1.png", frame_duration),
	("resources/characters/bbm_back2.png", frame_duration),
	("resources/characters/bbm_back1.png", frame_duration),
	("resources/characters/bbm_back3.png", frame_duration),
	])
player_left = PygAnimation([
	("resources/characters/bbm_left1.png", frame_duration),
	("resources/characters/bbm_left2.png", frame_duration),
	("resources/characters/bbm_left1.png", frame_duration),
	("resources/characters/bbm_left3.png", frame_duration),
	])
player_right = PygAnimation([
	("resources/characters/bbm_right1.png", frame_duration),
	("resources/characters/bbm_right2.png", frame_duration),
	("resources/characters/bbm_right1.png", frame_duration),
	("resources/characters/bbm_right3.png", frame_duration),
	])

conductor = PygConductor(player_down, player_up, player_left, player_right)

# initially animation are in stopped state so nothing will be drawn
# so we call pause so it will be drawn
conductor.pause()

current_direction = "down"

while not gameExit:
	gameDisplay.blit(arena, (0,0))
	for event in pygame.event.get():
		#exitting game
		if event.type == pygame.QUIT:
			gameExit = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -3
				y_change = 0
				conductor.stop()
				player_left.play()
				player_left.nextFrame()
				current_direction = "left"
				print("LEFT KEY PRESSED")
			if event.key == pygame.K_RIGHT:
				x_change = 3
				y_change = 0
				conductor.stop()
				player_right.play()
				player_right.nextFrame()
				current_direction = "right"
				print("RIGHT KEY PRESSED")
			if event.key == pygame.K_UP:
				y_change = -3
				x_change = 0
				conductor.stop()
				player_up.play()
				player_up.nextFrame()
				current_direction = "up"
				print("UP KEY PRESSED")
			if event.key == pygame.K_DOWN:
				y_change = 3
				x_change = 0
				player_down.play()
				player_down.nextFrame()
				current_direction = "down"
				print("DOWN KEY PRESSED")

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_change = 0
				y_change = 0
				conductor.pause_reset()
				# player_front.pause_reset()
				print("LEFT KEY UP")
			if event.key == pygame.K_RIGHT:
				x_change = 0
				y_change = 0
				conductor.pause_reset()
				# player_front.pause_reset()
				print("RIGHT KEY UP")
			if event.key == pygame.K_UP:
				y_change = 0
				x_change = 0
				conductor.pause_reset()
				# player_front.pause_reset()
				print("UP KEY UP")
			if event.key == pygame.K_DOWN:
				y_change = 0
				x_change = 0
				conductor.pause_reset()
				# player_front.pause_reset()
				print("DOWN KEY UP")

	# TODO: remove
	if x_move > 650: x_move = 650
	if x_move < 21: x_move = 21
	if y_move > 545: y_move = 545
	if y_move < 0: y_move = 0

	if current_direction is "down":
		player_down.blit(gameDisplay, (x_move, y_move))
	elif current_direction is "up":
		player_up.blit(gameDisplay, (x_move, y_move))
	elif current_direction is "left":
		player_left.blit(gameDisplay, (x_move, y_move))
	elif current_direction is "right":
		player_right.blit(gameDisplay, (x_move, y_move))

	x_move += x_change
	y_move += y_change

	# img = pygame.image.load('resources/characters/bomber_bazooka.gif').convert()

	# gameDisplay.fill((255,255,255))
	# pygame.draw.rect(gameDisplay, (0,0,0), [x_move, y_move, 100, 100])
	# gameDisplay.blit(img, (0,0))

	# map = pygame.Surface((765,675))
	# for x in range(0, 17):
	# 	for y in range (0, 15):
	# 		map.blit(grass_tile, (x * 45, y * 45))

	# arena = Arena((765, 675))

	# gameDisplay.blit(arena, (0,0))

	# a = pygame.sprite.Sprite()

	# gameDisplay.blit(map,(0,0))

	pygame.display.update()

	clock.tick(60)


pygame.quit()
quit()