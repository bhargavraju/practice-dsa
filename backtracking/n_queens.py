"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer A, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate
a queen and an empty space respectively.
"""


# @param A : integer
# @return a list of list of strings
def solveNQueens(A):
    def is_safe(prev, col):
        for i in range(len(prev)):
            if prev[i] == col or len(prev) - i == abs(col - prev[i]):
                return False
        return True

    def rec_helper(row, prev, res, n):
        for j in range(n):
            if is_safe(prev, j):
                if row == n - 1:
                    res.append(prev + [j])
                    return
                rec_helper(row + 1, prev + [j], res, n)

    solutions = []
    rec_helper(0, [], solutions, A)
    ans = [["." * col + "Q" + "." * (A - 1 - col) for col in sol] for sol in solutions]
    return ans
