#!/usr/bin/python3
"""N-queens module.
"""

import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_number_error_and_exit():
    print("N must be a number")
    sys.exit(1)

def print_size_error_and_exit():
    print("N must be at least 4")
    sys.exit(1)

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    This function checks the row on the left side, the upper diagonal on the left side,
    and the lower diagonal on the left side to ensure no other queens are placed that
    would threaten the queen at board[row][col].

    Args:
        board (list of list of int): The chessboard represented as a 2D list where 1 indicates
                                     the presence of a queen and 0 indicates an empty space.
        row (int): The row index where the queen is to be placed.
        col (int): The column index where the queen is to be placed.

    Returns:
        bool: True if it's safe to place the queen at board[row][col], False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens_util(board, col):
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

def print_solution(board):
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens_util(board, 0):
        print("No solution exists")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit()
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()
    if N < 4:
        print_size_error_and_exit()
    solve_nqueens(N)
