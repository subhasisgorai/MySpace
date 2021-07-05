from math import sqrt
from itertools import product
from pprint import pprint


def solve_sudoku(board):

    def solve_partial_sudoku(i, j):
        if i == len(board):
            i = 0
            j += 1
            if j == len(board[i]):
                return True
            
        if not board[i][j] == empty_cell:
            return solve_partial_sudoku(i + 1, j)

        def valid_to_add(i, j, val):
            if any(val == board[k][j] for k in range(len(board))):
                return False
            if val in board[i]: return False
            region_size = int(sqrt(len(board)))
            curr_region_vert, curr_region_horz = i // region_size, j // region_size
            return not any(
                    val == board[region_size * curr_region_vert + a]
                                    [region_size * curr_region_horz + b]
                        for a, b in product(range(region_size), repeat=2)
                )

        for val in range(1, len(board) + 1):
            val = str(val)
            if valid_to_add(i, j, val):
                board[i][j] = val
                if solve_partial_sudoku(i + 1, j): return True

        board[i][j] = empty_cell
        return False
             
    empty_cell = '.'
    result = solve_partial_sudoku(0, 0)
    print('Could solve? {}'.format('Yes' if result else 'No'))


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print 'Initial state of the board:'
    pprint(board, width=100)
    solve_sudoku(board)
    pprint(board, width=100)
        
