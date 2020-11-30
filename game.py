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
