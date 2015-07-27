import pygame
from util import *
from tiles import *
from pygame import Surface
from pygame.sprite import Sprite
from pyganim import *
from physics import Physics
from game_settings import *
from arena import Arena

pygame.init()

game_display = pygame.display.set_mode((765,675))
pygame.display.set_caption('Bomberman')

pygame.display.update()

gameExit = False

clock = pygame.time.Clock()

x_move = 0
y_move = 0

x_change = 0
y_change = 0

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

p = Physics()

arena = Arena()

while not gameExit:
    arena.draw(game_display)
    for event in pygame.event.get():
        #exitting game
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # x_change = -3
                # y_change = 0
                # player_left.play()
                player_left.nextFrame()
                # current_direction = "left"
                # print("LEFT KEY PRESSED")
            if event.key == pygame.K_RIGHT:
                # x_change = 3
                # y_change = 0
                # player_right.play()
                player_right.nextFrame()
                # current_direction = "right"
                # print("RIGHT KEY PRESSED")
            if event.key == pygame.K_UP:
                # y_change = -3
                # x_change = 0
                # player_up.play()
                player_up.nextFrame()
                # current_direction = "up"
                # print("UP KEY PRESSED")
            if event.key == pygame.K_DOWN:
                # y_change = 3
                # x_change = 0
                # player_down.play()
                player_down.nextFrame()
                # current_direction = "down"
                # print("DOWN KEY PRESSED")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                conductor.pause_reset()
                # player_front.pause_reset()
                # print("LEFT KEY UP")
            if event.key == pygame.K_RIGHT:
                conductor.pause_reset()
                # player_front.pause_reset()
                # print("RIGHT KEY UP")
            if event.key == pygame.K_UP:
                conductor.pause_reset()
                # player_front.pause_reset()
                # print("UP KEY UP")
            if event.key == pygame.K_DOWN:
                conductor.pause_reset()
                # player_front.pause_reset()
                # print("DOWN KEY UP")
            y_change = 0
            x_change = 0

    # TODO: remove
    if x_move > RIGHT_BORDER_X: x_move = RIGHT_BORDER_X
    if x_move < LEFT_BORDER_X: x_move = LEFT_BORDER_X
    if y_move > DOWN_BORDER_Y: y_move = DOWN_BORDER_Y
    if y_move < UP_BORDER_Y: y_move = UP_BORDER_Y


    if current_direction is "down":
        x_move, y_move = p.resolve_player_collision(x_move, y_move, current_direction)
        player_down.blit(game_display, (x_move, y_move))
    elif current_direction is "up":
        if pygame.key.get_pressed()[pygame.K_UP]:
            x_move, y_move = p.resolve_player_collision(x_move, y_move, current_direction)
        player_up.blit(game_display, (x_move, y_move))
    elif current_direction is "left":
        x_move, y_move = p.resolve_player_collision(x_move, y_move, current_direction)
        player_left.blit(game_display, (x_move, y_move))
    elif current_direction is "right":
        x_move, y_move = p.resolve_player_collision(x_move, y_move, current_direction)
        player_right.blit(game_display, (x_move, y_move))

    print("( ", x_move, " , ", y_move, ")")
    
    x_move += x_change
    y_move += y_change

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and \
        not keys[pygame.K_DOWN] and \
        not keys[pygame.K_LEFT] and \
        not keys[pygame.K_RIGHT]:
            y_change = -3
            x_change = 0
            current_direction = "up"
            player_up.play()
            # pass
            # print("UP PRESSED")
    if keys[pygame.K_RIGHT] and \
        not keys[pygame.K_UP] and \
        not keys[pygame.K_LEFT] and \
        not keys[pygame.K_DOWN]:
            x_change = 3
            y_change = 0
            current_direction = "right"
            player_right.play()
            # pass
            # print("RIGHT PRESSED")
    if keys[pygame.K_DOWN] and \
        not keys[pygame.K_UP] and \
        not keys[pygame.K_RIGHT] and \
        not keys[pygame.K_LEFT]:
            y_change = 3
            x_change = 0
            current_direction = "down"
            player_down.play()
            # pass
            # print("DOWN PRESSED")
    if keys[pygame.K_LEFT] and \
        not keys[pygame.K_UP] and \
        not keys[pygame.K_RIGHT] and \
        not keys[pygame.K_DOWN]:
            x_change = -3
            y_change = 0
            current_direction = "left"
            player_left.play()
            # pass
            # print("LEFT PRESSED")

    pygame.display.update()

    sec = clock.tick(FPS)


pygame.quit()
quit()