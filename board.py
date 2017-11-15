SYMBOLS = '123456789'
EMPTY = '0'

class Board:
    def __init__(self):
        self.squares

    def assignSquare(self, square, symbol):
        square.setValue(symbol)
        print(self)

    def emptySquare(self, square):
        self.assignSquare(square, EMPTY)

    def getEmptySquares(self):
        # TODO: Return array of empty squares or False if any

    def isSolved(self):
        # TODO: Return if board is solved

    def __str__(self):
        # TODO: Print board
