from game import Game

class OfflineGame(Game):
    def __init__(self, game_display):
        Game.__init__(self, game_display)

    def run(self):
        Game.run(self)