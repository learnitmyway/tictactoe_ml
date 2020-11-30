import random

from game import get_available_actions


class AI():

    def choose_action(self, board):
        available_actions = list(get_available_actions(board))
        return random.choice(available_actions)
