EMPTY = None

X = "X"
O = "O"


def get_player(board):
    xCount = sum(i.count(X) for i in board)
    oCount = sum(i.count(O) for i in board)
    return O if xCount > oCount else X


def get_winner(board):

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


def is_over(board):
    for row in board:
        for col in row:
            if col == EMPTY:
                return False

    return True


def get_available_actions(board):
    actions = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                actions.add((i, j))
    return actions


class Game():

    def __init__(self):
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

    def apply_action(self, action):
        row, col = action
        self.board[row][col] = get_player(self.board)
