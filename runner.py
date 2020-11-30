from game import Game

game = Game()
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

    row = int(input("Choose row (0-index): "))
    col = int(input("Choose column (0-index): "))
    game.move((row, col))
