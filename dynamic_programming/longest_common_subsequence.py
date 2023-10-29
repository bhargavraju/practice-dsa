"""
Given two strings A and B. Find the longest common subsequence
( A sequence which does not need to be contiguous), which is common in both
the strings.
You need to return the length of such longest common subsequence.

Problem Constraints
1 <= Length of A, B <= 1005
"""


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(B)
        common_ss = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] == B[j-1]:
                    common_ss[i][j] = common_ss[i-1][j-1] + 1
                else:
                    common_ss[i][j] = max(common_ss[i][j-1], common_ss[i-1][j])
        return common_ss[n][m]
