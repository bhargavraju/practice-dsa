"""
Given two sequences A and B, count number of unique ways in sequence A, to
form a subsequence that is identical to the sequence B.

Subsequence : A subsequence of a string is a new string which is formed from
the original string by deleting some (can be none) of the characters without
disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Problem Constraints
1 <= length(A), length(B) <= 700

Example Input
Input 1:
 A = "abc"
 B = "abc"
Input 2:
 A = "rabbbit"
 B = "rabbit"

Example Output
Output 1:
 1
Output 2:
 3

Example Explanation
Explanation 1:
 Both the strings are equal.
Explanation 2:
 These are the possible removals of characters:
    => A = "ra_bbit"
    => A = "rab_bit"
    => A = "rabb_it"

 Note: "_" marks the removed character.
"""


# There are two cases, whether A[i] is present in the matching subsequences
# or not
# (i) If A[i] (the last char) is present, then it is filling for the last char
# in B, we have to pick j-1 chars of B from i-1 chars of A, so no of such
# combinations is dp[i-1][j-1]
# (ii) If A[i] is not present, then it is the same as picking j chars in B from
# i-1 chars in A so, such combinations are dp[i-1][j]
#
# The 1st scenario is not possible if A[i] != B[j]


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        a = len(A)
        b = len(B)
        if b > a:
            return 0
        dp = [[0] * (b + 1) for _ in range(a + 1)]
        for i in range(a + 1):
            dp[i][0] = 1
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[a][b]
