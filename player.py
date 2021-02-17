import math
import random

class Player:
    def __init__(self, letter):
        # x or o
        self.letter = letter

    # we want all players to get their next move
    def get_move(self, move):
        pass


class RandomComputerPlayer(Player):
    def __init__ (self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.availabel_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid square. Try again!')

        return val    

