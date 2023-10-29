"""
Given a matrix of integers A of size N x M and multiple queries Q, for each query find and return the submatrix sum.
Inputs to queries are top left (b, c) and bottom right (d, e) indexes of sub matrix whose sum is to find out.

NOTE:
Rows are numbered from top to bottom and columns are numbered from left to right.
Sum may be large so return the answer mod 109 + 7.

Problem Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
1 <= Q <= 100000
1 <= B[i] <= D[i] <= N
1 <= C[i] <= E[i] <= M
"""


def solve(A, B, C, D, E):
    n, m = len(A), len(A[0])
    q = len(B)
    for i in range(n):
        for j in range(1, m):
            A[i][j] += A[i][j - 1]
    for j in range(m):
        for i in range(1, n):
            A[i][j] += A[i - 1][j]
    ans = [0] * q
    for i in range(q):
        top, left, bottom, right = B[i] - 1, C[i] - 1, D[i] - 1, E[i] - 1
        ans[i] = A[bottom][right]
        if left > 0:
            ans[i] -= A[bottom][left - 1]
        if top > 0:
            ans[i] -= A[top - 1][right]
        if left > 0 and top > 0:
            ans[i] += A[top - 1][left - 1]
        ans[i] = ans[i] % 1000000007
    return ans
