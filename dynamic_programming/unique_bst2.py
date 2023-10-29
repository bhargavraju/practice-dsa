"""
Given an integer A, how many structurally unique BST's (binary search trees)
exist that can store values 1…A?

Example Input
Input 1:
 1
Input 2:
 2

Example Output
Output 1:
 1
Output 2:
 2

Example Explanation
Explanation 1:
 Only single node tree is possible.
Explanation 2:
 2 trees are possible, one rooted at 1 and other rooted at 2.
"""

# Catalan number


# @param A : integer
# @return an integer
def numTrees(A):
    dp = [0]*(A+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, A+1):
        for j in range(i):
            dp[i] += dp[j]*dp[i-1-j]
    return dp[A]
