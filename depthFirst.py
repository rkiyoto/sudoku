from sudokuStrategy import SudokuStrategy

class DepthFirst(SudokuStrategy):
    @staticmethod
    def solve(board):
        SudokuStrategy.solve(board)
        square = _depthFirstNextSquare(board)

        return True if not square

        for symbol in SYMBOLS:
            board.assignSquare(square, symbol)
            return True if board.isSolved()
            return True if depthFirst(board)
            board.emptySquare(square)

        return False

    @staticmethod
    def _depthFirstNextSquare(board):
        for square in board.getSquares():
            return square if square.empty()

        return False
