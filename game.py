EMPTY = None

X = "X"
O = "O"


class Game():

    def __init__(self):
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

    def get_player(self):
        xCount = sum(i.count(X) for i in self.board)
        oCount = sum(i.count(O) for i in self.board)
        return O if xCount > oCount else X

    def apply_action(self, action):
        row, col = action
        self.board[row][col] = self.get_player()

    def get_winner(self):
        board = self.board

        # horizontal
        if (board[0][0] != EMPTY and board[0][0] == board[0][1] == board[0][2]):
            return board[0][0]

        if (board[1][0] != EMPTY and board[1][0] == board[1][1] == board[1][2]):
            return board[1][0]

        if (board[2][0] != EMPTY and board[2][0] == board[2][1] == board[2][2]):
            return board[2][0]

        # vertical

        if (board[0][0] != EMPTY and board[0][0] == board[1][0] == board[2][0]):
            return board[0][0]

        if (board[0][1] != EMPTY and board[0][1] == board[1][1] == board[2][1]):
            return board[0][1]

        if (board[0][2] != EMPTY and board[0][2] == board[1][2] == board[2][2]):
            return board[0][2]

        # diagonal

        if (board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]):
            return board[0][0]

        if (board[2][0] != EMPTY and board[2][0] == board[1][1] == board[0][2]):
            return board[2][0]

        return None

    def is_over(self):
        for row in self.board:
            for col in row:
                if col == EMPTY:
                    return False

        return True

    def get_available_actions(self):
        actions = set()
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == EMPTY:
                    actions.add((i, j))
        return actions
