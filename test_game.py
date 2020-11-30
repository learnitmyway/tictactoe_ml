import pytest
from game import Game

EMPTY = None

X = "X"
O = "O"


class TestGame:
    def test_get_player_first_move(self):
        assert Game().get_player() == X

    def test_get_player_O(self):
        game = Game()
        game.board = [
            [EMPTY, O, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, X, EMPTY]
        ]

        assert game.get_player() == O

    def test_get_player_X(self):
        game = Game()
        game.board = [
            [O, EMPTY, EMPTY],
            [EMPTY, EMPTY, X],
            [EMPTY, EMPTY, EMPTY]
        ]

        assert game.get_player() == X

    def test_move(self):
        game = Game()
        game.board = [
            [O, EMPTY, O],
            [EMPTY, EMPTY, X],
            [X, EMPTY, EMPTY]
        ]

        game.move((0, 1))

        expected_board = [
            [O, X, O],
            [EMPTY, EMPTY, X],
            [X, EMPTY, EMPTY]
        ]
        assert game.board == expected_board

    def test_get_winner_none(self):
        game = Game()
        game.board = [
            [EMPTY, EMPTY, EMPTY],
            [O, X, EMPTY],
            [O, X, EMPTY]
        ]

        assert game.get_winner() == None

    def test_get_winner(self):
        game = Game()
        game.board = [
            [EMPTY, X, EMPTY],
            [O, X, EMPTY],
            [O, X, EMPTY]
        ]

        assert game.get_winner() == X

    def test_is_over_false(self):
        game = Game()
        game.board = [
            [EMPTY, X, EMPTY],
            [O, X, EMPTY],
            [O, X, EMPTY]
        ]

        assert game.is_over() == False

    def test_is_over_true(self):
        game = Game()
        game.board = [
            [X, O, X],
            [O, X, X],
            [O, X, O]
        ]

        assert game.is_over() == True
