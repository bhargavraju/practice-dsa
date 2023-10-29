"""
Reverse the bits of an 32 bit unsigned integer A.
"""


def reverse(A):
    rev = 0
    for i in range(32):
        rev = rev << 1
        if A & 1 == 1:
            rev = rev | 1
        A = A >> 1
    return rev
