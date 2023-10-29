"""
Given a string A. Find the longest palindromic subsequence (A subsequence
which does not need to be contiguous and is a palindrome). You need to return
the length of the longest palindromic subsequence.

Problem Constraints
1 <= length of(A) <= 10^3
"""


def solve(A):
    n = len(A)
    dp = [[1] * n for _ in range(n)]
    for i in range(n - 1):
        if A[i] == A[i + 1]:
            dp[i][i + 1] = 2
    for i in range(n - 3, -1, -1):
        for j in range(i + 2, n):
            if A[i] == A[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]
