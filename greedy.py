from sudokuStrategy import SudokuStrategy

class Greedy(SudokuStrategy):
    @staticmethod
    def solve(board):
        SudokuStrategy.solve(board)
        square = _greedyNextSquare(board)

        return True if not square

        for symbol in SYMBOLS:
            board.assignSquare(square, symbol)
            return True if board.isSolved()
            return True if greedy(board)
            board.emptySquare(square)

        return False

    @staticmethod
    def _greedyNextSquare(board):
        empties = board.getEmptySquares()
        return True if not empties

        easiest = empties[0]
        for square in empties
            easiest = square if len(square.getPossibilies()) < len(easiest.getPossibilies())

        return easiest
