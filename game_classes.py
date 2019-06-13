import random 
from dice import Dice

class Player:
    
    def __init__(self, is_person=False):
        self.is_person = is_person

    def make_choice(self, temp_score):
        if not self.is_person:
            print(f"NPC current temp score is {temp_score}")
            if temp_score < 20:
                return True
            False
        else:
            keep_rolling = "p"
            while keep_rolling[0].lower() != "y" and keep_rolling[0].lower() != "n":
                keep_rolling = input(f"your current temp score is {temp_score} do you want to continue rolling? [y/n]")
            return keep_rolling.lower().startswith("y")

class Gamecon:

    def __init__(self, players_list):
        self.players_list = players_list
    
    def player_turn(self, player, total_score=0):
        """
        given a player it has the player roll, gets the result from Dice, stores the teporary score, displays
         it to the player and if the player wants to roll again resrtarts that loop. Once the player's turn ends 
         it adds the temporary score to their total_score 
        """
        temp_score = 0
        d6 = Dice()
        roller = self.players_list[player-1]
        roll_on = True
        while roll_on == True:
            current_roll =0
            current_roll += d6.roll()
            print(f"You rolled a {current_roll}!")
            if current_roll == 1:
                print("Better luck next time.")
                return 0
            temp_score += current_roll
            roll_on = roller.make_choice(temp_score)
        return temp_score

    def choose_first_player(self):
        """
        initializes the game, rolls a die to determine who goes first.
        """
        game_start_int = Dice(len(self.players_list)).roll()
        print(game_start_int)
        # first_player_turn = self.players_list[game_start_int-1]
        print(f"Player {game_start_int} goes first.")
        # return first_player_turn
        return game_start_int


    def game_state(self):
        """
        detects if a player has won the game, stores  current_scores
        """
        total_score_dict = {}
        for player in range(len(self.players_list)):
            total_score_dict[player] = [(player+1), 0]
        print("score dict:", total_score_dict)
        first_player = self.choose_first_player()
        current_player = first_player
        print("current player: ", current_player)
        turn_score = self.player_turn(current_player)
        print("turn score =:", turn_score)
        total_score_dict[player] += turn_score
        print(total_score_dict)
        # print("this?", first_player)