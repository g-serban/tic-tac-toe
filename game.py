import player

class TicTacToe:
    def __init__(self, board):
        self.board = [' ' for _ in range(9)]  # we will use a single list to repr a 3x3 board
        self.winner = None  # keep track of the winner in this game

    def print_board(self):
        # this is getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
 
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self):
        # if valid move, then make the move (assign square to letter)
        # then return value. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] == letter
            return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'x' # starting letter
    # iterate while the game still has empty squares 
    while game.empty_squares():
        # get the move from the appropiate player
        if letter = '0':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define a function to make a move
        letter = '0' if letter == 'X' else 'X' # switches player




