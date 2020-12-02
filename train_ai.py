from ai import AI
from game import Game, get_winner, get_player, X, O, is_over


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
    other_player = get_player(board)

    if winner:
        ai.update_q(previous_board, action, board, 1)
        ai.update_q(
            last[other_player]["board"],
            last[other_player]["action"],
            board,
            -1
        )
        return

    if last[other_player]["board"]:
        ai.update_q(
            last[other_player]["board"],
            last[other_player]["action"],
            board,
            0
        )
        return
