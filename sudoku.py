#!/usr/bin/env python3
from board import SYMBOLS

def depthFirstNextSquare(board):
    for square in board.getSquares():
        return square if square.empty()

    return False

def depthFirst(board):
    square = depthFirstNextSquare(board)

    return True if not square

    for symbol in SYMBOLS:
        board.assignSquare(square, symbol)
        return True if board.isSolved()
        return True if depthFirst(board)
        board.emptySquare(square)

    return False

def greedyNextSquare(board):
    empties = board.getEmptySquares()
    return True if not empties

    easiest = empties[0]
    for square in empties
        easiest = square if len(square.getPossibilies()) < len(easiest.getPossibilies())

    return easiest

def greedy(board):
    square = greedyNextSquare(board)

    return True if not square

    for symbol in SYMBOLS:
        board.assignSquare(square, symbol)
        return True if board.isSolved()
        return True if greedy(board)
        board.emptySquare(square)

    return False
