#!/usr/local/bin/python3

def matrix_sum(matrix, opt=False):
    """
    Given a 2D matrix, return a matrix with sum of previously seen values in each cell.
    'Previously seen' is determined by a left to right, top to bottom scan.

    >>> matrix_sum([[1, 2, 3], [4, 5, 6]])
    [[1, 3, 6], [5, 12, 21]]
    >>> matrix_sum([[1, 2, 3], [4, 5, 6]], opt=True)
    [[1, 3, 6], [5, 12, 21]]
    """
    rows = len(matrix)
    columns = len(matrix[0])
    b = [[0 for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            if not opt:
                b[i][j] = matrix[i][j] + \
                            sum([matrix[i][l] for l in range(j)]) + \
                            (b[i-1][j] if i > 0 else 0)
            else:
                b[i][j] = matrix[i][j] + \
                          (b[i-1][j] if i > 0 else 0) + \
                          (b[i][j-1] if j > 0 else 0) - \
                          (b[i-1][j-1] if (i > 0 and j > 0) else 0)   

    return b

if __name__ == '__main__':
    size = 400
    a = [[x for x in range(size)] for _ in range(size)]
    b = matrix_sum(a, True)

