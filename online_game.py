from game import Game
from client import Client
from network_events import Event

class OnlineGame(Game):
    def __init__(self, game_display):
        Game.__init__(self, game_display)
        self.client = Client(game_display)

    def run(self):
        if self.client.connected() is False:
            pygame.quit()
            quit()

        self.client.run()
        Game.run(self)

    def send_player_action(self, player_action):
        if player_action is not None:
            self.client.send_packet(encode(player_action))

            if player_action == Event.EXIT:
                pygame.quit()
                quit()