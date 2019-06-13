from dice import Dice
from game_classes import Gamecon, Player


test_game = Gamecon()
player1 = Player(True)
player2 = Player()
test_players_list = [player1, player2]
print(test_game.choose_first_player(test_players_list))