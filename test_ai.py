import pytest
import mock

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
