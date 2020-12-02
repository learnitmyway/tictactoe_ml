import pytest
import mock

from train_ai import update_ai
from ai import AI
from game import Game, get_winner, get_player, X, O, is_over, EMPTY


class TestTrainAI:
    def test_update_ai(self):
        game = Game()

        previous_board = [
            [X, X, EMPTY],
            [O, O, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

        board = [
            [X, X, X],
            [O, O, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]
        game.board = board

        action = (0, 2)

        last = {
            X: {"board": board, "action": action},
            O: {"board": previous_board, "action": (1, 2)}
        }

        winner = get_winner(board)
        ai = AI()

        update_ai(previous_board, game, winner, ai, action, last)

        # TODO: assert ai.update_q was called twice with the correct arguments
