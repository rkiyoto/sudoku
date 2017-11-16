#!/usr/bin/env python3
from board import SYMBOLS
from board import Board
import sys

from depthFirst import DepthFirst
from greedy import Greedy
from sudokuStrategy import SudokuStrategy

strategies = [SudokuStrategy]

# Parse CLI options
if len(sys.argv) == 1 :
    print("To run " + sys.arv[0] + " pass a file name where each line is a sudoku game with 81 characters per line and optionally an output file name")

inputFile = open(sys.argv[1])

if len(sys.argv) >= 3:
    outputFile = open(sys.argv[2], 'w')
    sys.stdout = outputFile

# Solve every sudoku setup on inputFile
for line in inputFile:
    for strategy in strategies:
        board = Board.fromString(line)
        strategy.solve(board)

inputFile.close()
outputFile.close() if outputFile
