import unittest
import pygame
from game_settings import *
from object import Object
from player import Player, Direction, PlayerState
from arena import Arena


class TestObject(unittest.TestCase):
    def test_object_position(self):
        object = Object((0, 22), 10, 20)
        self.assertEqual(object.position(), (0, 22))

    def test_object_width(self):
        object = Object((12, 23), 5, 8)
        self.assertEqual(object.get_width(), 5)

    def test_object_height(self):
        object = Object((88, 54), 345, 334)
        self.assertEqual(object.get_height(), 334)

    def test_object_get_x(self):
        object = Object((122, 45), 47, 33)
        self.assertEqual(object.get_x(), 122)

    def test_object_get_y(self):
        object = Object((876, 123), 65, 6)
        self.assertEqual(object.get_y(), 123)

    def test_move_left(self):
        object = Object((100, 100), 43, 33)
        object.move_left(5)

        self.assertEqual(object.get_x(), 95)

    def test_move_right(self):
        object = Object((443, 1123), 65, 498)
        object.move_right(10)

        self.assertEqual(object.get_x(), 453)

    def test_move_up(self):
        object = Object((50, 50), 12, 10)
        object.move_up(2)

        self.assertEqual(object.get_y(), 48)

    def test_move_down(self):
        object = Object((12, 22), 12, 10)
        object.move_up(2)

        self.assertEqual(object.get_y(), 20)

    def test_is_intersected(self):
        first_object = Object((0, 0), 5, 5)
        second_object = Object((10, 10), 5, 5)

        self.assertEqual(
            first_object.is_intersected_with(second_object), False)

    def test_contains_point(self):
        object = Object((0, 0), 10, 10)
        self.assertEqual(object.contains_point((5, 5)), True)
        self.assertEqual(object.contains_point((11, 11)), False)

    def test_set_position(self):
        object = Object((10, 10), 33, 11)
        object.set_position((1, 1))

        self.assertEqual(object.position(), (1, 1))

    def test_normalize_position(self):
        object = Object((22, 0), 33, 11)
        self.assertEqual(object.normalize_position(), (0, 1))

    def test_normalize_position_for_explosion(self):
        object = Object((112, 0), 33, 11)
        self.assertEqual(object.normalize_position(), (0, 3))

    def test_in_first_column(self):
        object = Object((22, 0), 33, 11)
        self.assertEqual(object._in_first_column(), True)

    def test_in_first_row(self):
        object = Object((322, 0), 33, 11)
        self.assertEqual(object._in_first_row(), True)


class TestPlayer(unittest.TestCase):
    def test_set_position(self):
        game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        arena = Arena()
        player = Player((0, 0), arena)
        player.set_player_position((22, 1))

        self.assertEqual(player.position(), (22, 1))

    def test_set_player_tile_position(self):
        game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        arena = Arena()
        player = Player((0, 0), arena)
        player.set_player_tile_position((90, 45))

        self.assertEqual(player.position(), (67, 0))

    def test_move_up(self):
        game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        arena = Arena()
        player = Player((10, 20), arena)
        player.move_up()

        self.assertEqual(player.position(), (10, 17))

    def test_move_left(self):
        game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        arena = Arena()
        player = Player((199, 0), arena)
        player.move_left()

        self.assertEqual(player.position(), (202, 0))

    def test_move_right(self):
        game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        arena = Arena()
        player = Player((15, 20), arena)
        player.move_right()

        self.assertEqual(player.position(), (18, 20))

    def test_move_down(self):
        game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        arena = Arena()
        player = Player((14, 80), arena)
        player.move_down()

        self.assertEqual(player.position(), (14, 83))

    def test_is_alive(self):
        game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        arena = Arena()
        player = Player((112, 0), arena)
        player.state = PlayerState.DEAD

        self.assertEqual(player.is_alive(), False)

    def test_current_state(self):
        game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        arena = Arena()
        player = Player((112, 0), arena)

        self.assertEqual(player.current_state(), PlayerState.ALIVE)

    def test_die(self):
        game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        arena = Arena()
        player = Player((112, 0), arena)
        player.die()

        self.assertEqual(player.is_alive(), False)

    def test_place_bomb(self):
        game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        arena = Arena()
        player = Player((112, 0), arena)
        player.place_bomb()

        self.assertEqual(player.placed_bomb, 1)

if __name__ == "__main__":
    unittest.main()
