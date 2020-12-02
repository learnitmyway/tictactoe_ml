import random
import numpy

from game import get_available_actions


class AI():
    def __init__(self):
        self.q = dict()
        self.alpha = 0.5

    def choose_action(self, board):
        available_actions = list(get_available_actions(board))
        return random.choice(available_actions)

    def update_q(self, board, action, new_board, reward):
        board_flat = list(numpy.array(board).flat)

        q = self.get_q(board_flat, action)

        available_actions = get_available_actions(new_board)
        new_board_flat = list(numpy.array(new_board).flat)
        future_reward = self.get_best_reward(available_actions, new_board_flat)

        self.q[tuple(board_flat), action] = q + self.alpha * \
            (reward + future_reward - q)

    def get_q(self, board, action):
        return self.q.get((tuple(board), action)) or 0

    def get_best_reward(self, available_actions, board_flat):
        best_q = -1
        for action in available_actions:
            q_val = self.get_q(board_flat, action)
            if (q_val > best_q):
                best_q = q_val

        return best_q
