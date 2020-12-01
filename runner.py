from game import Game, EMPTY, X, O, get_player, is_over, get_winner, get_available_actions
from train_ai import train_ai

game = Game()
ai = train_ai()

while True:
    print("Board: ")
    for row in game.board:
        print(row)

    winner = get_winner(game.board)
    if winner:
        print("Winner:")
        print(winner)
        break

    if is_over(game.board):
        print("Game Over. No winner")
        break

    print("Player's turn:")
    player = get_player(game.board)
    print(player)

    if player == 'X':
        game.apply_action(ai.choose_action(game.board))
    else:
        row = int(input("Choose row (0-index): "))
        col = int(input("Choose column (0-index): "))
        game.apply_action((row, col))
