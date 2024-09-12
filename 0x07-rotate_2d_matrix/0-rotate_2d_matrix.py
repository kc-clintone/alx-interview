#!/usr/bin/python3
"""
Rotating a 2D matrix.
"""


def rotate_2d_matrix(matrix):
    """
    This implementation rotates a 2D matrix (m*n)
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    columns = len(matrix[0])
    if not all(map(lambda k: len(k) == columns, matrix)):
        return
    col, row = 0, rows - 1
    for j in range(columns * rows):
        if j % rows == 0:
            matrix.append([])
        if row == -1:
            row = rows - 1
            col += 1
        matrix[-1].append(matrix[row][col])
        if col == columns - 1 and row >= -1:
            matrix.pop(row)
        row -= 1
