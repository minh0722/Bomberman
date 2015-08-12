from pyganim import PygAnimation
from game_settings import *
from util import *


def create_bomb():
    return PygAnimation([
        (TILE_RESOURCE_PATH + "normal_bomb_1.png", BOMB_FRAME_DURATION),
        (TILE_RESOURCE_PATH + "normal_bomb_2.png", BOMB_FRAME_DURATION),
        (TILE_RESOURCE_PATH + "normal_bomb_3.png", BOMB_FRAME_DURATION),
        (TILE_RESOURCE_PATH + "normal_bomb_4.png", BOMB_FRAME_DURATION),
        (TILE_RESOURCE_PATH + "normal_bomb_1.png", BOMB_FRAME_DURATION),
        (TILE_RESOURCE_PATH + "normal_bomb_2.png", BOMB_FRAME_DURATION),
        (TILE_RESOURCE_PATH + "normal_bomb_3.png", BOMB_FRAME_DURATION),
        (TILE_RESOURCE_PATH + "normal_bomb_4.png", BOMB_FRAME_DURATION)],
        loop=False)


def create_center_explosion():
    return PygAnimation([
        (EXPLOSION1_RESOURCE_PATH + "explosion_center.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION2_RESOURCE_PATH + "explosion_center.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION1_RESOURCE_PATH + "explosion_center.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION2_RESOURCE_PATH + "explosion_center.png",
            EXPLOSION_FRAME_DURATION)],
        loop=False)


def create_left_explosion():
    return PygAnimation([
        (EXPLOSION1_RESOURCE_PATH + "explosion_left.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION2_RESOURCE_PATH + "explosion_left.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION1_RESOURCE_PATH + "explosion_left.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION2_RESOURCE_PATH + "explosion_left.png",
            EXPLOSION_FRAME_DURATION)],
        loop=False)


def create_right_explosion():
    return PygAnimation([
        (EXPLOSION1_RESOURCE_PATH + "explosion_right.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION2_RESOURCE_PATH + "explosion_right.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION1_RESOURCE_PATH + "explosion_right.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION2_RESOURCE_PATH + "explosion_right.png",
            EXPLOSION_FRAME_DURATION)],
        loop=False)


def create_up_explosion():
    return PygAnimation([
        (EXPLOSION1_RESOURCE_PATH + "explosion_up.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION2_RESOURCE_PATH + "explosion_up.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION1_RESOURCE_PATH + "explosion_up.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION2_RESOURCE_PATH + "explosion_up.png",
            EXPLOSION_FRAME_DURATION)],
        loop=False)


def create_down_explosion():
    return PygAnimation([
        (EXPLOSION1_RESOURCE_PATH + "explosion_down.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION2_RESOURCE_PATH + "explosion_down.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION1_RESOURCE_PATH + "explosion_down.png",
            EXPLOSION_FRAME_DURATION),

        (EXPLOSION2_RESOURCE_PATH + "explosion_down.png",
            EXPLOSION_FRAME_DURATION)],
        loop=False)


def create_player_down():
    return PygAnimation([
        ("resources/characters/bbm_front1.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_front2.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_front1.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_front3.png", PLAYER_FRAME_DURATION)
        ])


def create_player_up():
    return PygAnimation([
        ("resources/characters/bbm_back1.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_back2.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_back1.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_back3.png", PLAYER_FRAME_DURATION),
        ])


def create_player_left():
    return PygAnimation([
        ("resources/characters/bbm_left1.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_left2.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_left1.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_left3.png", PLAYER_FRAME_DURATION),
        ])


def create_player_right():
    return PygAnimation([
        ("resources/characters/bbm_right1.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_right2.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_right1.png", PLAYER_FRAME_DURATION),
        ("resources/characters/bbm_right3.png", PLAYER_FRAME_DURATION),
        ])


def create_player_die():
    return PygAnimation([
        ("resources/characters/bbm_die1.png", PLAYER_DIE_FRAME_DURATION),
        ("resources/characters/bbm_die2.png", PLAYER_DIE_FRAME_DURATION),
        ("resources/characters/bbm_die3.png", PLAYER_DIE_FRAME_DURATION),
        ("resources/characters/bbm_die4.png", PLAYER_DIE_FRAME_DURATION)],
        loop=False)


def create_destroying_wall_sprites():
    return PygAnimation([
        (TILE_RESOURCE_PATH + "tile_destroyed_1.png",
            WALL_DESTROYED_FRAME_DURATION),

        (TILE_RESOURCE_PATH + "tile_destroyed_2.png",
            WALL_DESTROYED_FRAME_DURATION),

        (TILE_RESOURCE_PATH + "tile_destroyed_3.png",
            WALL_DESTROYED_FRAME_DURATION),

        (TILE_RESOURCE_PATH + "tile_destroyed_4.png",
            WALL_DESTROYED_FRAME_DURATION),

        (TILE_RESOURCE_PATH + "tile_destroyed_5.png",
            WALL_DESTROYED_FRAME_DURATION),

        (TILE_RESOURCE_PATH + "tile_destroyed_6.png",
            WALL_DESTROYED_FRAME_DURATION)],
        loop=False)


def create_destructible_wall_image():
    return load_image(
            "battle_tiles/battle_stage_1/destructible_tile.png").convert()
