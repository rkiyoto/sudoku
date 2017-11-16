from board import EMPTY
from board import SYMBOLS

class Square:
    def __init__(self, code, units, peers):
        # Positional info
        self.code = code
        self.units = units
        self.peers = peers

        # Sudoku value info
        self.value = EMPTY
        self.possibilities = SYMBOLS.remove(symbol)

    def getPossibilies(self):
        return self.possibilities

    def getUnits(self):
        return self.units

    def getPeers(self):
        return self.peers

    def getValue(self):
        return sefl.value

    def setValue(self, value):
        self.value = value

    def isEmpty(self):
        return self.value == EMPTY
