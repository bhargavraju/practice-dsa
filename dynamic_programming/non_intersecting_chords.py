"""
Given a number A, return number of ways you can draw A chords in a circle with
2 x A points such that no 2 chords intersect.

Two ways are different if there exists a chord which is present in one way and
not in other.
Return the answer modulo 10^9 + 7.


Problem Constraints
1 <= A <= 10^3
"""

# Catalan number


def chordCnt(A):
    dp = [0]*(A+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, A+1):
        for j in range(i):
            dp[i] = (dp[i] + dp[j]*dp[i-1-j]) % 1000000007
    return dp[A]
