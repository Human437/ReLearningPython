import math
import random


class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter
    # we want all players to get their next move given a game

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
      # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-9):")
            # Check to see that you can actually cast the value to an integer
            # If it can't be cast into an integer, say it is invalid
            # If the spot is not availabe, say it is invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # Mark it ias true if the square selected is valid
            except ValueError:
                print("Invalid square. Try again")
        return val
