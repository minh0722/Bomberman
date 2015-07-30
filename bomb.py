from object import Object
from game_settings import *


class Bomb(Object):
    def __init__(self, x, y, bomb_range):
        Object.__init__(self, x, y)

        self.range = bomb_range
        self.state = 'TICKING'
        
        self.bomb_sprite = PygAnimation([
            ("resources/battle_tiles/battle_stage_1/normal_bomb_1.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_2.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_3.png", BOMB_FRAME_DURATION),
            ("resources/battle_tiles/battle_stage_1/normal_bomb_4.png", BOMB_FRAME_DURATION)
            ])

        

    def draw(self, game_display):
        pass