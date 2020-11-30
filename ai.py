import random


class AI():
    def choose_action(self, board):
        i = random.randrange(len(board))
        j = random.randrange(len(board[0]))
        return (i, j)
