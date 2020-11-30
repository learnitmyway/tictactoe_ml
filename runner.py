from game import Game
from ai import AI

game = Game()
ai = AI(game)

while True:
    print("Board: ")
    for row in game.board:
        print(row)

    winner = game.get_winner()
    if winner:
        print("Winner:")
        print(winner)
        break

    if game.is_over():
        print("Game Over. No winner")
        break

    print("Player's turn:")
    player = game.get_player()
    print(player)

    if player == 'X':
        game.apply_action(ai.choose_action())
    else:
        row = int(input("Choose row (0-index): "))
        col = int(input("Choose column (0-index): "))
        game.apply_action((row, col))
