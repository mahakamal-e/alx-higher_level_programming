#!/usr/bin/python3
""" N queens module """

import sys


def check_safe(board, row, col):
    """ Check if any queens threaten the current position"""
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def Recursive_func(N, column, board, result):
    """ Recursive function to solve the N-queens
    problem using backtracking
    """
    if column == N:
        result.append([board[i] for i in range(N)])
        return

    for row in range(N):
        if check_safe(board, row, column):
            board[column] = row
            Recursive_func(N, column + 1, board, result)

def solveNQueens(N):
    """
    Main function to solve the N Queens problem
    """
    if N < 4:
        print("N must be at least 4")
        return

    board = [-1] * N
    result = []
    Recursive_func(N, 0, board, result)

    if not result:
        print("No solution exists")
    else:
        for res in result:
            print(res)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solveNQueens(N)

