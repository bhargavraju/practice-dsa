"""
Given a matrix of integers A of size N x 2 describing dimensions of N
envelopes, where A[i][0] denotes the height of the ith envelope and A[i][1]
denotes the width of the ith envelope.

One envelope can fit into another if and only if both the width and height of
one envelope is greater than the width and height of the other envelope.

Find the maximum number of envelopes you can put one inside other.

Example Input
Input 1:
 A = [
         [5, 4]
         [6, 4]
         [6, 7]
         [2, 3]
     ]
Input 2:
 A = [     '
         [8, 9]
         [8, 18]
     ]

Example Output
Output 1:
 3
Output 2:
 1

Example Explanation
Explanation 1:
 Step 1: put [2, 3] inside [5, 4]
 Step 2: put [5, 4] inside [6, 7]
 3 envelopes can be put one inside other.
Explanation 2:
 No envelopes can be put inside any other so answer is 1.
"""

# Similar to largest increasing subsequence


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort(key=lambda x: (x[0], x[1]))
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if A[i][0] > A[j][0] and A[i][1] > A[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
