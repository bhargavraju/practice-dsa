"""
Given two integer arrays A and B of size N each which represent values and
weights associated with N items respectively. Also given an integer C which
represents knapsack capacity. Find out the maximum value subset of A such that
sum of the weights of this subset is smaller than or equal to C.

NOTE: You cannot break an item, either pick the complete item, or
don’t pick it (0-1 property).

Problem Constraints
1 <= N <= 500
1 <= C, B[i] <= 10^6
1 <= A[i] <= 50
"""


# Issue with traditional knapsack approach her is the constraints. Since the
# max possible value for each weight is 10^6, time complexity would be too high
# So we use value as the second dimension with dp[i][j] representing the min
# weight necessary to achieve 'j' profit/value with i elements

# first column is 0 as to achieve 0 profit/value, we need 0 min weight
# first row is infinite as to achieve positive profit/value with no elements
# is not possible and is represented by infinite capacity


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(A)
        max_value = sum(A)
        dp = [[float('inf')]*(max_value+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(1, n+1):
            for j in range(1, max_value+1):
                if A[i-1] <= j:
                    dp[i][j] = min(dp[i-1][j], B[i-1] + dp[i-1][j-A[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
        for j in range(max_value, -1, -1):
            if dp[n][j] <= C:
                return j
