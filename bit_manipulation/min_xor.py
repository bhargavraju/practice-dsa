"""
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value.
Report the minimum XOR value.

Problem Constraints
2 <= length of the array <= 100000
0 <= A[i] <= 10^9
"""


def findMinXor(A):
    A.sort()
    min_xor = A[0] ^ A[1]
    for i in range(1, len(A) - 1):
        xor = A[i] ^ A[i + 1]
        min_xor = min(min_xor, xor)
    return min_xor
