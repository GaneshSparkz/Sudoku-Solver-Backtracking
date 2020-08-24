from sudoku import Sudoku


# initialize the 9x9 puzzle board
board = [
    [0, 0, 6, 0, 1, 0, 0, 0, 0],
    [8, 0, 5, 2, 0, 0, 0, 7, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [3, 5, 1, 0, 6, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 5, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 0],
    [9, 0, 0, 1, 5, 0, 4, 6, 0],
    [0, 0, 0, 3, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 0, 7],
]

# instantiate the Sudoku puzzle
puzzle = Sudoku(board, n_rows=9, n_cols=9)

print("[INFO] The given Sudoku puzzle...")
puzzle.print_board()

print("[INFO] Solving the puzzle...")
puzzle.solve()
print("[INFO] Solved...")

print("[INFO] The solution of the puzzle is...")
puzzle.print_board()
