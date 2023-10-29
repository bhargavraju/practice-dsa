"""
Given an array of integers A, sort the array into a wave like array and return it, In other words,
arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

NOTE : If there are multiple answers possible, return the one that's lexicographically smallest.

Problem Constraints
1 <= len(A) <= 106
1 <= A[i] <= 106
"""


def wave(A):
    A.sort()
    for i in range(0, len(A), 2):
        if i + 1 < len(A):
            A[i], A[i + 1] = A[i + 1], A[i]
    return A
