from dice import Dice
from game_classes import Gamecon, Player

d20_x_1 = Dice(20)
d5_x_3 = Dice(5,3)

print(d20_x_1, d5_x_3)
player1 = Player(True)
player2 = Player()
test_players_list = [player1, player2]

test_game = Gamecon(test_players_list)
test_game.game_state()
# print(test_game.choose_first_player(test_players_list))