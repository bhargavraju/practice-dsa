"""
Given A, B, C find whether C is formed by the interleaving of A and B.

Problem Constraints
1 <= length(A), length(B) <= 100
1 <= length(C) <= 200

Input Format
The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains a string, C.
"""


# @param A : string
# @param B : string
# @param C : string
# @return an integer
def isInterleave(A, B, C):
    a, b, c = len(A), len(B), len(C)
    if c != a + b:
        return 0
    dp = [[0]*(b+1) for _ in range(a+1)]
    for i in range(a+1):
        for j in range(b+1):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0 and B[j-1] == C[i+j-1]:
                dp[i][j] = dp[i][j-1]
            elif j == 0 and A[i-1] == C[i+j-1]:
                dp[i][j] = dp[i-1][j]
            elif A[i-1] == C[i+j-1] and B[j-1] != C[i+j-1]:
                dp[i][j] = dp[i-1][j]
            elif A[i-1] != C[i+j-1] and B[j-1] == C[i+j-1]:
                dp[i][j] = dp[i][j-1]
            elif A[i-1] == C[i+j-1] and B[j-1] == C[i+j-1]:
                dp[i][j] = dp[i][j-1] | dp[i-1][j]
    return dp[a][b]

