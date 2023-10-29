"""
Given a M x N grid A of integers, find a path from top left to bottom right
which minimizes the sum of all numbers along its path.

Return the minimum sum of the path.

NOTE: You can only move either down or right at any point in time.


Problem Constraints
1 <= M, N <= 2000
-1000 <= A[i][j] <= 1000
"""


# @param A : list of list of integers
# @return an integer
def minPathSum(A):
    m = len(A)
    n = len(A[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                A[i][j] += A[i][j-1]
            elif j == 0:
                A[i][j] += A[i-1][j]
            else:
                A[i][j] += min(A[i-1][j], A[i][j-1])
    return A[m-1][n-1]
