from sudokuStrategy import SudokuStrategy
from square import SYMBOLS
import os
clear = lambda: os.system('clear')
empties = []

class DepthFirst(SudokuStrategy):
    @staticmethod
    def solve(board):
        # SETUP
        global empties
        empties = board.getEmptySquares()
        DepthFirst._search(board)


    @staticmethod
    def _search(board):
        global empties
        SudokuStrategy.solve(board)
        square = DepthFirst._depthFirstNextSquare(board)
        if not square:
            return True

        for i, symbol in enumerate(SYMBOLS):
            # print(square.code, symbol)
            board.assignSquare(square, symbol)
            if (square.code == empties[0].code or square.code == empties[1].code):
                print(square.code, symbol)

            if board.isSolved():
                return True
            if board.isValid():
                if DepthFirst._search(board):
                    return True

            board.emptySquare(square)

        empties.insert(0, square)
        return False

    @staticmethod
    def _depthFirstNextSquare(board):
        global empties

        return empties.pop(0)
