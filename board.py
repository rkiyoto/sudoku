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
            [cross(rowSection, columnSection) for rowSection in ('123','456','789') for columnSection in ('ABC','DEF','GHI')])

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
        for peerCode in square.getPeers():
            peer = self.squares[peerCode]
            setOfValues = set([self.squares[peerOfpeerCode].value for peerOfpeerCode in peer.getPeers()])
            if symbol != EMPTY:
                setOfValues.add(symbol)
            setOfValues = set(SYMBOLS) - setOfValues
            values = ''.join(setOfValues).replace(EMPTY, '')
            peer.setPossibilities(str(values))

        # print(self)

    def emptySquare(self, square):
        self.assignSquare(square, EMPTY)

    def getEmptySquares(self):
        # Return array of empty squares or False if any
        return [square for square in self.squares.values() if square.isEmpty()]

    def isValid(self):
        def unitvalid(unit):
            unitvalues = [str(self.squares[s]) for s in unit]
            unitvalues = [value for value in unitvalues if value != EMPTY]
            
            # print(len(unitvalues) == len(set(unitvalues)), unitvalues, set(unitvalues))
            return len(unitvalues) == len(set(unitvalues))
        return all(unitvalid(unit) for unit in UNIT_LIST)

    def isSolved(self):
        "A puzzle is solved if each unit is a permutation of the digits 1 to 9."
        def unitsolved(unit): return set(str(self.squares[s]) for s in unit) == set(SYMBOLS)
        return self.squares is not False and all(unitsolved(unit) for unit in UNIT_LIST)

    @staticmethod
    def fromString(string):
        board = Board()

        for i, code in enumerate(SQUARE_CODES):
            board.assignSquare(board.squares[code], string[i])

        return board

    def __str__(self):
        toString = ""
        for col in COLS:
            for row in ROWS:
                toString += str(self.squares[row+col])

        # toString = "-"*37+"\n"
        # for i, row in enumerate(ROWS):
        #     toString += ("|" + " {}   {}   {} |"*3).format(*[str(self.squares[row+col]) for col in COLS])+"\n"
        #     if i == 8:
        #         toString += "-"*37
        #     elif i % 3 == 2:
        #         toString += "|" + "---+"*8 + "---|\n"
        #     else:
        #         toString += "|" + "   +"*8 + "   |\n"

        return toString
