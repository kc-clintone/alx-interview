#!/usr/bin/python3
"""
Let's play a little chess.
"""

import sys


def print_solution(board):
    """
    Print the board configuration for the N-Queens problem.

    Each solution is represented as a list of lists, where each list contains
    two integers: the row and column index of a queen.

    Parameters:
    board (list of list of int): 2D list representing the chessboard.
    """
    solution = [[i, row.index(1)] for i, row in enumerate(board)]
    print(solution)

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    A queen can be attacked by another queen if they share the same row, column, or diagonal.

    Parameters:
    board (list of list of int): 2D list representing the chessboard.
    row (int): Row index.
    col (int): Column index.

    Returns:
    bool: True if it's safe to place the queen, False otherwise.
    """
    if 1 in board[row][:col]:
        return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col):
    """
    Utilizes backtracking to place queens on the board.

    This function attempts to place queens one by one in different columns
    and uses backtracking to find all possible solutions.

    Parameters:
    board (list of list of int): 2D list representing the chessboard.
    col (int): Current column to attempt placing a queen.

    Returns:
    bool: True if a solution is found, False otherwise.
    """
    if col >= len(board):
        print_solution(board)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0

    return res

def solve_nqueens(N):
    """
    Solves the N-Queens problem by initializing the chessboard and starting the backtracking process.

    Parameters:
    N (int): The size of the chessboard (N x N).
    """
    board = [[0] * N for _ in range(N)]
    if not solve_nqueens_util(board, 0):
        print("No solution exists")

def validate_input(args):
    """
    Validates the command-line arguments to ensure the correct usage of the program.

    Parameters:
    args (list of str): List of command-line arguments.

    Returns:
    int: The validated size of the chessboard (N).
    """
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(args[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


if __name__ == "__main__":
    N = validate_input(sys.argv)
    solve_nqueens(N)
