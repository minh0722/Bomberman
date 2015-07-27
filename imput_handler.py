import pygame

class InputHandler:
	def __init__(self, player):
		self.player = player

	def handle_input(self, pygame_event):
		if event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_LEFT:
	            player_left.nextFrame()
	        if event.key == pygame.K_RIGHT:
	            player_right.nextFrame()
	        if event.key == pygame.K_UP:
	            player_up.nextFrame()
	        if event.key == pygame.K_DOWN:
	            player_down.nextFrame()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.pause_reset()
            if event.key == pygame.K_RIGHT:
                player.pause_reset()
            if event.key == pygame.K_UP:
                player.pause_reset()
            if event.key == pygame.K_DOWN:
                player.pause_reset()