"""
Given an array of integers A and an integer B. Find and return the maximum value of | s1 - s2 |
where s1 = sum of any subset of size B, s2 = sum of elements of A - sum of elements of s1

Note |x| denotes the absolute value of x.
"""


def solve(A, B):
    A.sort()
    max_diff = 0
    max_diff = max(max_diff, abs(sum(A[:B]) - sum(A[B:])))
    max_diff = max(max_diff, abs(sum(A[-B:]) - sum(A[:-B])))
    return max_diff
