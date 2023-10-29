"""
Given a string A containing just the characters '(' and ')'.
Find the length of the longest valid (well-formed) parentheses substring.

Problem Constraints
1 <= length(A) <= 750000
"""


# @param A : string
# @return an integer
def longestValidParentheses(A):
    n = len(A)
    dp = [0] * n

    for r in range(1, n):
        if A[r] != ')':
            continue
        l = r - 1 - dp[r - 1]
        if l >= 0 and A[l] == '(':
            dp[r] = r - l + 1
            if l > 0:
                dp[r] += dp[l - 1]

    return max(dp)
