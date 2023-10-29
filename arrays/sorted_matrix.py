"""
Given a matrix of integers A of size N x M and an integer B.
In the given matrix every row and column is sorted in increasing order. Find and return the position of B in the matrix
in the given form:
If A[i][j] = B then return (i * 1009 + j)
If B is not present return -1.

Note 1: Rows are numbered from top to bottom and columns are numbered from left to right.
Note 2: If there are multiple B in A then return the smallest value of i*1009 +j such that A[i][j]=B.


Problem Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
-100000 <= B <= 100000
"""


def solve(A, B):
    m, n = len(A), len(A[0])
    top, right = 0, n - 1
    while top < m and right >= 0:
        if A[top][right] == B:
            if right - 1 >= 0 and A[top][right - 1] == B:
                right -= 1
                continue
            else:
                return (top+1) * 1009 + (right+1)
        elif A[top][right] > B:
            right -= 1
        elif A[top][right] < B:
            top += 1
    return -1


ans = solve([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
], 2)
print(ans)
