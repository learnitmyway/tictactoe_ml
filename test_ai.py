import pytest
import mock

from ai import AI
from game import EMPTY, X, O


class TestAI:
    @mock.patch('random.randrange')
    def test_choose_action_first_choice(self, randrange_mock):
        randrange_mock.side_effect = [0, 1]

        board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

        assert AI().choose_action(board) == (0, 1)
