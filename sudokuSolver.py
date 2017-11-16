#!/usr/bin/env python3
import sys

from board import Board

from depthFirst import DepthFirst
from greedy import Greedy
from sudokuStrategy import SudokuStrategy

strategies = [DepthFirst]

# Parse CLI options
if len(sys.argv) == 1 :
    print("To run " + sys.argv[0] + " pass a file name(puzzles.txt) where each line is a sudoku game with 81 characters per line and optionally an output file name")
    sys.exit()

inputFile = open(sys.argv[1])

if len(sys.argv) >= 3:
    outputFile = open(sys.argv[2], 'w')
    sys.stdout = outputFile

# Solve every sudoku setup on inputFile
for line in inputFile:
    for strategy in strategies:
        print("Solving sudoku board using " + strategy.__name__ + " strategy:")
        print("")
        board = Board.fromString(line)
        strategy.solve(board)
        print("")

inputFile.close()
if 'outputFile' in locals():
    outputFile.close()
