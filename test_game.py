import pytest

from game import Game, EMPTY, X, O, get_player, is_over, get_winner, get_available_actions


class TestGame:
    def test_get_player_first_move(self):
        board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]
        assert get_player(board) == X

    def test_get_player_O(self):
        board = [
            [EMPTY, O, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, X, EMPTY]
        ]

        assert get_player(board) == O

    def test_get_player_X(self):
        board = [
            [O, EMPTY, EMPTY],
            [EMPTY, EMPTY, X],
            [EMPTY, EMPTY, EMPTY]
        ]

        assert get_player(board) == X

    def test_apply_action(self):
        game = Game()
        game.board = [
            [O, EMPTY, O],
            [EMPTY, EMPTY, X],
            [X, EMPTY, EMPTY]
        ]

        game.apply_action((0, 1))

        expected_board = [
            [O, X, O],
            [EMPTY, EMPTY, X],
            [X, EMPTY, EMPTY]
        ]
        assert game.board == expected_board

    def test_get_winner_none(self):
        board = [
            [EMPTY, EMPTY, EMPTY],
            [O, X, EMPTY],
            [O, X, EMPTY]
        ]

        assert get_winner(board) == None

    def test_get_winner(self):
        board = [
            [EMPTY, X, EMPTY],
            [O, X, EMPTY],
            [O, X, EMPTY]
        ]

        assert get_winner(board) == X

    def test_is_over_false(self):
        board = [
            [EMPTY, X, EMPTY],
            [O, X, EMPTY],
            [O, X, EMPTY]
        ]

        assert is_over(board) == False

    def test_is_over_true(self):
        board = [
            [X, O, X],
            [O, X, X],
            [O, X, O]
        ]

        assert is_over(board) == True

    def test_get_available_actions(self):
        board = [
            [EMPTY, EMPTY, EMPTY],
            [O, X, EMPTY],
            [O, X, EMPTY]
        ]

        expected = {(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)}
        assert get_available_actions(board) == expected
