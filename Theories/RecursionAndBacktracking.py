"""
Recursion and Backtracking: Theory and Implementation
"""

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    def solve(row, board, solutions):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row+1, board, solutions)
    solutions = []
    solve(0, [0]*n, solutions)
    return solutions

'''
Use Cases:
- Solving puzzles (N-Queens, Sudoku)
- Generating permutations/combinations
- Divide and conquer algorithms
- Pathfinding (maze, backtracking)
'''
