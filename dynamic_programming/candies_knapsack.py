"""
Rishik likes candies a lot. So, he went to a candy-shop to buy candies. The
shopkeeper showed him N packets each containg A[i] candies for cost of C[i]
nibbles, each candy in that packet has a sweetness B[i]. The shopkeeper puts
the condition that Rishik can buy as many complete candy-packets as he wants
but he can't buy a part of the packet.

Rishik has D nibbles, can you tell him the maximum amount of sweetness he can
get from candy-packets he will buy?


Problem Constraints
1 <= N <= 700
1 <= A[i] <= 1000
1 <= B[i] <= 1000
1 <= C[i],D <= 1000
"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        n = len(A)
        dp = [0]*(D+1)
        for i in range(1, D+1):
            for j in range(n):
                if C[j] <= i:
                    dp[i] = max(dp[i], A[j]*B[j] + dp[i-C[j]])
        return dp[D]
