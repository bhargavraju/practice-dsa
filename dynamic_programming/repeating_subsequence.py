"""
Given a string A, find if there is any subsequence that repeats itself.

A subsequence of a string is defined as a sequence of characters generated by
deleting some characters in the string without changing the order of the
remaining characters.

NOTE: Subsequence length should be greater than or equal to 2.

Problem Constraints
1 <= length(A) <= 100
"""

# Same as longest_common_subsequence except that both strings are same and
# the indexes should be different when if it is to be considered a match


class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        n = len(A)
        ways = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if A[i - 1] == A[j - 1] and i != j:
                    ways[i][j] = ways[i - 1][j - 1] + 1
                else:
                    ways[i][j] = max(ways[i - 1][j], ways[i][j - 1])

        if ways[n][n] >= 2:
            return 1
        return 0