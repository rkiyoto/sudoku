from square import Square
from square import SYMBOLS
from square import EMPTY


ROWS = '123456789'
COLS = 'ABCDEFGHI'

# Section of code was copied from https://github.com/norvig/pytudes/blob/master/py/sudoku.py
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

SQUARE_CODES  = cross(ROWS, COLS)
UNIT_LIST = ([cross(ROWS, column) for column in COLS] +
            [cross(row, COLS) for row in ROWS] +
            [cross(rowSection, columnSection) for rowSection in ('ABC','DEF','GHI') for columnSection in ('123','456','789')])

UNITS = dict((s, [u for u in UNIT_LIST if s in u])
             for s in SQUARE_CODES)
PEERS = dict((s, set(sum(UNITS[s],[]))-set([s]))
             for s in SQUARE_CODES)

# End of copied code from https://github.com/norvig/pytudes/blob/master/py/sudoku.py

class Board:
    def __init__(self):
        # Create a dictonary that maps each square code to a Square with its units and peers
        self.squares = dict(
                        (code, Square(code, UNITS[code], PEERS[code]))
                        for code in SQUARE_CODES
                    )

    def assignSquare(self, square, symbol):
        square.setValue(symbol)
        print(self)

    def emptySquare(self, square):
        self.assignSquare(square, EMPTY)

    def getEmptySquares(self):
        # Return array of empty squares or False if any
        return [square for square in self.squares.values() if square.isEmpty()]

    def isSolved(self):
        # TODO: Return if board is solved
        return True

    @staticmethod
    def fromString(string):
        board = Board()

        for i, code in enumerate(SQUARE_CODES):
            board.squares[code].setValue(string[i])

        return board

    def __str__(self):
        toString = ""
        for y in ROWS:
            for x in COLS:
                toString += str(self.squares[y+x])

        return toString
