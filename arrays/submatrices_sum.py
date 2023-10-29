"""
Given a 2D Matrix A of dimensions N*N, we need to return sum of all possible submatrices.

Problem Constraints
1 <= N <=30
0 <= A[i][j] <= 10
"""


def solve(A):
    m, n = len(A), len(A[0])
    total = 0
    for i in range(m):
        for j in range(n):
            total += (i + 1) * (j + 1) * (m - i) * (n - j) * A[i][j]
    return total
