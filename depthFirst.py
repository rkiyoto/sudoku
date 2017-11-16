from sudokuStrategy import SudokuStrategy

class DepthFirst(SudokuStrategy):
    @staticmethod
    def solve(board):
        SudokuStrategy.solve(board)
        square = _depthFirstNextSquare(board)

        if not square:
            return True

        for symbol in SYMBOLS:
            board.assignSquare(square, symbol)
            
            if board.isSolved():
                return True
            if depthFirst(board):
                return True

            board.emptySquare(square)

        return False

    @staticmethod
    def _depthFirstNextSquare(board):
        for square in board.getSquares():
            if square.empty():
                return square

        return False
