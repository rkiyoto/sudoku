SYMBOLS = '123456789'
EMPTY = '0'

class Square:
    def __init__(self, code, units, peers):
        # Positional info
        self.code = code
        self.units = units
        self.peers = peers

        # Sudoku value info
        self.value = EMPTY
        self.possibilities = SYMBOLS

    def removePossibility(self, symbol):
        try:
            self.possibilities = self.possibilities.remove(symbol)
        except:
            pass

    def setPossibilities(self, possibilities):
        self.possibilities = possibilities

    def getPossibilies(self):
        return self.possibilities

    def getUnits(self):
        return self.units

    def getPeers(self):
        return self.peers

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def isEmpty(self):
        return self.value == EMPTY

    def __str__(self):
        return str(self.value)
