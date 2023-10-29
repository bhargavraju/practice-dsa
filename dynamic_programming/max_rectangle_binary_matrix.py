"""
Given a 2-D binary matrix A of size N x M filled with 0's and 1's, find the
largest rectangle containing all ones and return its area.

Problem Constraints
1 <= N, M <= 100
"""


# @param A : list of list of integers
# @return an integer
def maximalRectangle(A):
    n = len(A)
    m = len(A[0])
    res = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1:
                A[i][j] = A[i][j] + A[i][j-1] if j > 0 else A[i][j]
                width = A[i][j]
                for k in range(i, -1, -1):
                    if A[k][j] == 0:
                        break
                    width = min(width, A[k][j])
                    res = max(res, (i-k+1)*width)
    return res
