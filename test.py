import pygame
from util import *
from tiles import *
from pygame import Surface
from pygame.sprite import Sprite
from pyganim import *
from physics import Physics

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

p = Physics()

while not gameExit:
    gameDisplay.blit(arena, (0,0))
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
                x_change = 0
                y_change = 0
                conductor.pause_reset()
                # player_front.pause_reset()
                # print("LEFT KEY UP")
            if event.key == pygame.K_RIGHT:
                x_change = 0
                y_change = 0
                conductor.pause_reset()
                # player_front.pause_reset()
                # print("RIGHT KEY UP")
            if event.key == pygame.K_UP:
                y_change = 0
                x_change = 0
                conductor.pause_reset()
                # player_front.pause_reset()
                # print("UP KEY UP")
            if event.key == pygame.K_DOWN:
                y_change = 0
                x_change = 0
                conductor.pause_reset()
                # player_front.pause_reset()
                # print("DOWN KEY UP")

    # TODO: remove
    if x_move > 652: x_move = 652
    if x_move < 22: x_move = 22
    if y_move > 540: y_move = 540
    if y_move < 0: y_move = 0


    wall_nodes_x = (22, 112)
    wall_nodes_y = (0, 90)

    # for row in range(0, 6):
    #     for column in range(0, 7):
    #         if x_move > 22 + row * 90 and x_move < 112 + row * 90 and \
    #            y_move > 0 + column * 90 and y_move < 90 + column * 90:
    #                 x_move = 22 + row * 90
    #                 y_move = 6 + column * 90
    #                 print(x_move)
            # print("Pos ( ", x_move, " , ", y_move, ")")

    if current_direction is "down":
        x_move, y_move = p.resolve_player_collision(x_move, y_move, current_direction)
        player_down.blit(gameDisplay, (x_move, y_move))
    elif current_direction is "up":
        x_move, y_move = p.resolve_player_collision(x_move, y_move, current_direction)
        player_up.blit(gameDisplay, (x_move, y_move))
    elif current_direction is "left":
        x_move, y_move = p.resolve_player_collision(x_move, y_move, current_direction)
        player_left.blit(gameDisplay, (x_move, y_move))
    elif current_direction is "right":
        x_move, y_move = p.resolve_player_collision(x_move, y_move, current_direction)
        player_right.blit(gameDisplay, (x_move, y_move))

    print("( ", x_move, " , ", y_move, ")")
    
    x_move += x_change
    y_move += y_change

    ##############################

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y_change = -3
        x_change = 0
        current_direction = "up"
        player_up.play()
        # pass
        # print("UP PRESSED")
    if keys[pygame.K_RIGHT]:
        x_change = 3
        y_change = 0
        current_direction = "right"
        player_right.play()
        # pass
        # print("RIGHT PRESSED")
    if keys[pygame.K_DOWN]:
        y_change = 3
        x_change = 0
        current_direction = "down"
        player_down.play()
        # pass
        # print("DOWN PRESSED")
    if keys[pygame.K_LEFT]:
        x_change = -3
        y_change = 0
        current_direction = "left"
        player_left.play()
        # pass
        # print("LEFT PRESSED")


    ###############################

    # img = pygame.image.load('resources/characters/bomber_bazooka.gif').convert()

    # gameDisplay.fill((255,255,255))
    # pygame.draw.rect(gameDisplay, (0,0,0), [x_move, y_move, 100, 100])
    # gameDisplay.blit(img, (0,0))

    # map = pygame.Surface((765,675))
    # for x in range(0, 17):
    #   for y in range (0, 15):
    #       map.blit(grass_tile, (x * 45, y * 45))

    # arena = Arena((765, 675))

    # gameDisplay.blit(arena, (0,0))

    # a = pygame.sprite.Sprite()

    # gameDisplay.blit(map,(0,0))

    pygame.display.update()

    sec = clock.tick(60)


pygame.quit()
quit()