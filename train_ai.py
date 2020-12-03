from ai import AI
from game import Game, get_winner, get_player, X, O, is_over
from copy import deepcopy


def train_ai():
    ai = AI()

    for i in range(10000):
        print(f"Playing training game {i + 1}")
        game = Game()

        last = {
            X: {"board": None, "action": None},
            O: {"board": None, "action": None}
        }

        while True:
            board_before_action = deepcopy(game.board)
            action = ai.choose_action(board_before_action)
            player = get_player(board_before_action)

            last[player]["board"] = board_before_action
            last[player]["action"] = action

            game.apply_action(action)

            winner = get_winner(game.board)

            update_ai(board_before_action, game, winner, ai, action, last)

            if is_over(game.board) or winner:
                break

    for board, action in ai.q.items():
        print(board)
        print(action)
    return ai


def update_ai(board_before_action, game, winner, ai, action, last):
    board_after_action = deepcopy(game.board)
    other_player = get_player(board_after_action)

    if winner:
        ai.update_q(board_before_action, action, board_after_action, 1)
        ai.update_q(
            last[other_player]["board"],
            last[other_player]["action"],
            board_after_action,
            -1
        )
        return

    if last[other_player]["board"]:
        ai.update_q(
            last[other_player]["board"],
            last[other_player]["action"],
            board_after_action,
            0
        )
        return
