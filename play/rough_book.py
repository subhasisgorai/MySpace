from copy import copy


def n_queens(n): 

    def get_queens_placement(row):
        if row == n:
            result.append(copy(col_placement))
            return 
        for col in range(n):
            if all(abs(col - c) not in (0, row - i)
                    for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                get_queens_placement(row + 1)
    
    result = list()
    col_placement = [0] * n
    get_queens_placement(0)
    return result


if __name__ == '__main__':
    print n_queens(4)
