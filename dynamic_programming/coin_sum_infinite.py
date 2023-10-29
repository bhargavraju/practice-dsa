"""
You are given a set of coins A. In how many ways can you make sum B assuming
you have infinite amount of each coin in the set.

NOTE:
Coins in set A will be unique. Expected space complexity of this problem is
O(B). The answer can overflow. So, return the answer % (10^6 + 7).
"""


# Since 'no of ways' is required, for f(n) consider all possible 'last steps'
# to reach n. In this case, we need to add all possible ways until before
# these last steps to reach n to get f(n)


# @param A : list of integers
# @param B : integer
# @return an integer
def coinchange2(A, B):
    dp = [0]*(B+1)
    dp[0] = 1
    n = len(A)
    for i in range(n):
        for j in range(A[i], B+1):
            dp[j] = (dp[j] + dp[j-A[i]]) % 1000007
    return dp[B]
