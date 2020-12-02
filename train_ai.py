from ai import AI
from game import Game, get_winner, get_player, X, O, is_over
import numpy


def train_ai():
    ai = AI()

    for i in range(100):
        print(f"Playing training game {i + 1}")
        game = Game()

        last = {
            X: {"board": None, "action": None},
            O: {"board": None, "action": None}
        }

        while True:
            board = game.board.copy()
            action = ai.choose_action(board)
            player = get_player(board)

            last[player]["board"] = board
            last[player]["action"] = action

            game.apply_action(action)

            winner = get_winner(game.board)

            update_ai(board, game, winner, ai, action, last)

            if is_over(game.board) or winner:
                break

    return ai


def update_ai(previous_board, game, winner, ai, action, last):
    board = game.board.copy()
    board_flat = list(numpy.array(board).flat)
    other_player = get_player(board)
    last_other_player_board_flat = list(
        numpy.array(last[other_player]["board"]).flat)

    if winner:
        previous_board_flat = list(numpy.array(previous_board).flat)
        ai.update_q(previous_board_flat, action, board_flat, 1)
        ai.update_q(
            last_other_player_board_flat,
            last[other_player]["action"],
            board_flat,
            -1
        )
        return

    if last[other_player]["board"]:
        ai.update_q(
            last_other_player_board_flat,
            last[other_player]["action"],
            board_flat,
            0
        )
        return
