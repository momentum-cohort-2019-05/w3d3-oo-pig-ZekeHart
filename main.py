from dice import Dice
from game_classes import Gamecon, Player


player1 = Player(True)
player2 = Player()
test_players_list = [player1, player2]

test_game = Gamecon(test_players_list)
test_game.game_state()
# print(test_game.choose_first_player(test_players_list))