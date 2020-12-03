import random
import numpy
import sys

from game import get_available_actions


class AI():
    def __init__(self):
        self.q = dict()
        self.alpha = 0.5

    def choose_action(self, board):
        available_actions = list(get_available_actions(board))

        board_flat = list(numpy.array(board).flat)

        best_q = -sys.maxsize - 1
        chosen_action = list(available_actions)[0]
        for action in available_actions:
            q_val = self.get_q(board_flat, action)
            if (q_val > best_q):
                best_q = q_val
                chosen_action = action

        return chosen_action

    def update_q(self, board, action, new_board, reward):
        board_flat = list(numpy.array(board).flat)

        q = self.get_q(board_flat, action)

        available_actions = get_available_actions(new_board)
        new_board_flat = list(numpy.array(new_board).flat)
        future_reward = self.get_best_reward(available_actions, new_board_flat)

        self.q[tuple(board_flat), action] = q + self.alpha * \
            (reward + future_reward - q)

    def get_q(self, board_flat, action):
        return self.q.get((tuple(board_flat), action)) or 0

    def get_best_reward(self, available_actions, board_flat):
        best_q = -sys.maxsize - 1
        for action in available_actions:
            q_val = self.get_q(board_flat, action)
            if (q_val > best_q):
                best_q = q_val

        return best_q
