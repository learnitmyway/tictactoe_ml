import pytest
import mock
import numpy

from ai import AI
from game import EMPTY, X, O


class TestAI:
    @mock.patch('random.choice')
    @pytest.mark.skip()
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

    def test_choose_action(self):
        board = [
            [O, O, X],
            [O, X, EMPTY],
            [X, X, EMPTY]
        ]
        board_flat = list(numpy.array(board).flat)

        ai = AI()

        ai.q[tuple(board_flat), (1, 2)] = -0.8
        ai.q[tuple(board_flat), (2, 2)] = 0.8

        action = ai.choose_action(board)

        assert action == (2, 2)

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
        new_board_flat = list(numpy.array(new_board).flat)

        ai = AI()

        reward = 0.6

        q = 0.4
        ai.q[tuple(board_flat), action] = q

        future_reward = 0.8
        ai.q[tuple(new_board_flat), (1, 2)] = -0.8
        ai.q[tuple(new_board_flat), (2, 2)] = future_reward

        ai.update_q(board, action, new_board, reward)

        assert ai.q.get((tuple(board_flat), action)) == q + \
            ai.alpha * (reward + future_reward - q)
