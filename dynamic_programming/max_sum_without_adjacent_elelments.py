"""
Given a 2 x N grid of integer, A, choose numbers such that the sum of the
numbers is maximum and no two chosen numbers are adjacent horizontally,
vertically or diagonally, and return it.
Note: You can choose more than 2 numbers.

Problem Constraints
1 <= N <= 20000
1 <= A[i] <= 2000
"""


# @param A : list of list of integers
# @return an integer
def adjacent(self, A):
    n = len(A[0])
    max_sum = [0] * (n + 1)
    max_sum[0] = 0
    max_sum[1] = max(A[0][0], A[1][0])
    for i in range(2, n + 1):
        max_sum[i] = max(max_sum[i - 1],
                         max_sum[i - 2] + max(A[0][i - 1], A[1][i - 1]))
    return max_sum[n]
