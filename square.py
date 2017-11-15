from board import EMPTY
from board import SYMBOLS

class Square:
    def __init__(self, symbol=EMPTY):
        self.value = symbol
        self.possibilities = SYMBOLS.remove(symbol)

    def getPossibilies(self):
        return self.possibilities

    def setValue(self, value):
        self.value = value

    def isEmpty(self):
        return self.value == EMPTY
