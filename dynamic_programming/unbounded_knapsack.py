"""
Given a knapsack weight A and a set of items with certain value B[i] and
weight C[i], we need to calculate maximum amount that could fit in this
quantity.

This is different from classical Knapsack problem, here we are allowed to use
unlimited number of instances of an item.

Problem Constraints
1 <= A <= 1000
1 <= |B| <= 1000
1 <= B[i] <= 1000
1 <= C[i] <= 1000
"""


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        dp = [0]*(A+1)
        n = len(B)
        for i in range(A + 1):
            for j in range(n):
                if C[j] <= i:
                    dp[i] = max(dp[i], dp[i - C[j]] + B[j])
        return dp[A]
