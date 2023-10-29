"""
Given an integer A.
Compute and return the square root of A.
If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.
"""


def sqrt(A):
    if A < 2:
        return A
    left, right, ans = 1, A, 1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == A:
            return mid
        elif mid * mid > A:
            right = mid - 1
        else:
            # If mid*mid < n, the number may be the floor of the square root or it may not be
            # So, store it before proceeding further
            ans = mid
            left = mid + 1
    return ans
