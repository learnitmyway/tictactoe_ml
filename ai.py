import random

from game import get_available_actions


class AI():
    def __init__(self):
        self.q = dict()
        self.alpha = 0.5

    def choose_action(self, board):
        available_actions = list(get_available_actions(board))
        return random.choice(available_actions)

    def update_q(self, board, action, new_board, reward):
        q = 0.5
        future_reward = 0.7
        self.q[tuple(board), action] = q + self.alpha * \
            (reward + future_reward - q)
