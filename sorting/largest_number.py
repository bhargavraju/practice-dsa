"""
Given a array A of non negative integers, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*109
"""

from functools import cmp_to_key


def largestNumber(A):
    def cmp_function(a, b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        return (ba > ab) - (ab > ba)

    l = sorted(A, key=cmp_to_key(cmp_function))
    i = 0
    while i < len(l) - 1 and l[i] == 0:
        i += 1
    return "".join(map(str, l[i:]))
