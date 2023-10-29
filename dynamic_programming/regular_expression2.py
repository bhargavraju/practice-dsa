"""
Implement wildcard pattern matching with support for ' ? ' and ' * ' for
strings A and B.

' . ' : Matches any single character.
' * ' : Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

1 <= length(A), length(B) <= 10^4


Input Format
The first argument of input contains a string A.
The second argument of input contains a string B denoting the pattern.

Output Format
Return 1 if the patterns match else return 0.
"""


# @param A : string
# @param B : string
# @return an integer
def isMatch(A, B):
    n = len(A)
    m = len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for j in range(2, m + 1):
        if B[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1] or B[j - 1] == ".":
                dp[i][j] = dp[i - 1][j - 1]
            elif B[j - 1] == "*":
                if B[j - 2] == A[i - 1] or B[j - 2] == ".":
                    dp[i][j] = dp[i][j - 2] | dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 2]

    return dp[n][m]
