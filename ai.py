import random


class AI():
    def get_next_move(self, board):
        i = random.randrange(len(board))
        j = random.randrange(len(board[0]))
        return (i, j)
