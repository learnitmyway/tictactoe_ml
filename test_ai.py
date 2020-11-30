import pytest
import mock

from ai import AI
from game import EMPTY, X, O


class TestAI:
    @mock.patch('random.randrange')
    def test_get_next_move_first_move(self, randrange_mock):
        randrange_mock.side_effect = [0, 1]

        board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

        assert AI().get_next_move(board) == (0, 1)
