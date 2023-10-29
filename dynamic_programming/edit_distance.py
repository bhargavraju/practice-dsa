"""
Given two strings A and B, find the minimum number of steps required to
convert A to B. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Problem Constraints
1 <= length(A), length(B) <= 450

Input Format
The first argument of input contains a string, A.
The second argument of input contains a string, B.

Output Format
Return an integer, representing the minimum number of steps required.
"""


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        n = len(A)
        m = len(B)
        min_steps = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            min_steps[i][0] = i
        for j in range(1, m+1):
            min_steps[0][j] = j
        for i in range(1, n+1):
            for j in range(1, m+1):
                if A[i-1] == B[j-1]:
                    min_steps[i][j] = min_steps[i-1][j-1]
                else:
                    min_steps[i][j] = min(min_steps[i-1][j] + 1,
                                          min_steps[i][j-1] + 1,
                                          min_steps[i-1][j-1] + 1)
        return min_steps[n][m]
