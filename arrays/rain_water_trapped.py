"""
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

Problem Constraints
1 <= |A| <= 100000
"""


def trap(A):
    n = len(A)
    left = [0] * n
    for i in range(1, n):
        left[i] = max(left[i - 1], A[i - 1])
    right = [0] * n
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], A[i + 1])
    water_trapped = 0
    for i in range(n):
        water_trapped += max(0, (min(left[i], right[i]) - A[i]))
    return water_trapped
