from sudokuStrategy import SudokuStrategy
from square import SYMBOLS

class DepthFirst(SudokuStrategy):
    @staticmethod
    def solve(board):
        SudokuStrategy.solve(board)
        square = DepthFirst._depthFirstNextSquare(board)

        if not square:
            return True

        for i, symbol in enumerate(SYMBOLS):
            board.assignSquare(square, symbol)

            if board.isSolved():
                return True
            if board.isValid():
                if DepthFirst.solve(board):
                    return True

            board.emptySquare(square)

        return False

    @staticmethod
    def _depthFirstNextSquare(board):
        for square in board.getEmptySquares():
            if square.isEmpty():
                return square

        return False
