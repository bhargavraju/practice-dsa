"""
Given a string A, partition A such that every substring of the partition is a
palindrome. Return the minimum cuts needed for a palindrome partitioning of A.


Problem Constraints
1 <= length(A) <= 501


Example Input
Input 1:
 A = "aba"
Input 2:
 A = "aab"


Example Output
Output 1:
 0
Output 2:
 1


Example Explanation
Explanation 1:
 "aba" is already a palindrome, so no cuts are needed.
Explanation 2:
 Return 1 since the palindrome partitioning ["aa","b"] could be produced
 using 1 cut.
"""


class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        n = len(A)

        pal_dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    pal_dp[i][j] = True
                elif j == i + 1:
                    if A[i] == A[j]:
                        pal_dp[i][j] = True
                else:
                    if pal_dp[i + 1][j - 1] and A[i] == A[j]:
                        pal_dp[i][j] = True

        cuts_dp = [i - 1 for i in range(1, n + 1)]
        for i in range(1, n):
            if pal_dp[0][i]:
                cuts_dp[i] = 0
                continue
            for j in range(i, 0, -1):
                if pal_dp[j][i]:
                    cuts_dp[i] = min(cuts_dp[i], cuts_dp[j - 1] + 1)

        return cuts_dp[n - 1]
