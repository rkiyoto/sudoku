from sudokuStrategy import SudokuStrategy
from square import SYMBOLS

class Greedy(SudokuStrategy):
    @staticmethod
    def solve(board):
        SudokuStrategy.solve(board)
        square = Greedy._greedyNextSquare(board)

        if not square:
            return True

        for symbol in SYMBOLS:
            board.assignSquare(square, symbol)
            if board.isSolved():
                return True

            if board.isValid():
                if Greedy.solve(board):
                    return True

            board.emptySquare(square)

        return False

    @staticmethod
    def _greedyNextSquare(board):
        empties = board.getEmptySquares()
        if not empties:
            return False

        easiest = empties[0]
        for square in empties:
            if len(square.getPossibilies()) < len(easiest.getPossibilies()):
                easiest = square

        return easiest
