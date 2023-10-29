"""
Given two integer arrays A and B of size N each which represent values and
weights associated with N items respectively. Also given an integer C which
represents knapsack capacity.

Find out the maximum value subset of A such that sum of the weights of this
subset is smaller than or equal to C.

NOTE:
You cannot break an item, either pick the complete item, or don’t pick it
(0-1 property).

Problem Constraints
1 <= N <= 10^3
1 <= C <= 10^3
1 <= A[i], B[i] <= 10^3
"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(A)
        dp = [[0]*(C+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for j in range(C+1):
            dp[0][j] = 0
        for i in range(1, n+1):
            for j in range(1, C+1):
                if B[i-1] <= j:
                    dp[i][j] = max(dp[i-1][j], A[i-1] + dp[i-1][j-B[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][C]
