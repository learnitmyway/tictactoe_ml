import random

from game import get_available_actions


class AI():
    def __init__(self):
        self.q = dict()
        self.alpha = 0.5

    def choose_action(self, board):
        available_actions = list(get_available_actions(board))
        return random.choice(available_actions)

    def update_q(self, board_flat, action, new_board_flat, reward):
        q = self.get_q(board_flat, action)
        future_reward = 0.7
        self.q[tuple(board_flat), action] = q + self.alpha * \
            (reward + future_reward - q)

    def get_q(self, board, action):
        return self.q.get((tuple(board), action)) or 0
