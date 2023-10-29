"""
Given a stack of integers A. You are required to reverse the stack using
recursion. You are not allowed to use loop constructs like while, for..etc,

Return A after reversing it using recursion.

1 <= length of the array <= 2000
1 <= A[i] <= 10^8
"""

import sys

sys.setrecursionlimit(2100)


def rec_helper(res, st):
    if len(st) == 0:
        return

    res.append(st.pop())
    return rec_helper(res, st)


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        res = []
        rec_helper(res, A)
        return res
