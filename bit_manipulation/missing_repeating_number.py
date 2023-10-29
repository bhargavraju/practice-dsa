"""
You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Note that in your output A should precede B.
"""


def repeatedNumber(A):
    n = len(A)
    xor = 0
    for num in A:
        xor ^= num
    for num in range(1, n + 1):
        xor ^= num
    last_bit_set = xor & ~(xor - 1)
    x, y = 0, 0
    for num in A:
        if num & last_bit_set != 0:
            x ^= num
        else:
            y ^= num
    for num in range(1, n + 1):
        if num & last_bit_set != 0:
            x ^= num
        else:
            y ^= num
    if x in A:
        return [x, y]
    else:
        return [y, x]
