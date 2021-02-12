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
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
    

