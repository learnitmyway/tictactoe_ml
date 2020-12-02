import pytest
import mock
import numpy

from ai import AI
from game import EMPTY, X, O


class TestAI:
    @mock.patch('random.choice')
    def test_choose_action_random(self, choice_mock):
        choice_mock.side_effect = self.get_first_arg

        board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

        action = AI().choose_action(board)
        call_args, _ = choice_mock.call_args

        assert action == call_args[0][0]

    def get_first_arg(self, *args):
        return args[0][0]

    def test_update_q(self):
        board = [
            [O, O, EMPTY],
            [O, X, EMPTY],
            [X, X, EMPTY]
        ]
        board_flat = list(numpy.array(board).flat)

        action = (0, 2)

        new_board = [
            [O, O, X],
            [O, X, EMPTY],
            [X, X, EMPTY]
        ]
        ai = AI()

        reward = 0.6

        q = 0.4
        ai.q[tuple(board_flat), action] = q

        ai.update_q(board, action, new_board, reward)

        future_reward = 0.7

        assert ai.q.get((tuple(board_flat), action)) == q + \
            ai.alpha * (reward + future_reward - q)
