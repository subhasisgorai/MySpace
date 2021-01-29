from copy import copy


def n_queens(n):

    def solve_n_queens(row):
        if row == n:
            result.append(copy(column_placement))
            return
        for col in range(n):
            if all(
                    abs(c - col) not in (0, row - i)
                    for i, c in enumerate(column_placement[:row])):
                column_placement[row] = col
                solve_n_queens(row + 1)

    result = []
    column_placement = [0] * n
    solve_n_queens(0)
    return result


if __name__ == '__main__':
    print n_queens(4)
