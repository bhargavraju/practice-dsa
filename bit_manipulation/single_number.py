"""
Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear
exactly twice. Find the two elements that appear only once.

Note: Output array must be sorted.

Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109
"""


def solve(A):
    xor = 0
    for num in A:
        xor ^= num
    last_set_bit = xor & ~(xor - 1)
    x, y = 0, 0
    for num in A:
        if num & last_set_bit != 0:
            x ^= num
        else:
            y ^= num
    return [x, y] if x < y else [y, x]
