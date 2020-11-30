from game import Game

game = Game()
print("Board: ")
for row in game.board:
    print(row)

print("X's Turn")
row = int(input("Choose row (0-index): "))
col = int(input("Choose column (0-index): "))
print("your move:")
print((row, col))
