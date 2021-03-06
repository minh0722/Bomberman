import pygame
from game_settings import *
from online_game import OnlineGame


def pygame_main():
    pygame.init()
    game_mainloop()


def game_mainloop():
    game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('BomberMin')

    game = OnlineGame(game_display)


    while True:
        game.run()

if __name__ == "__main__":
    pygame_main()
