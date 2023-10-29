"""
Given an array A of N integers, find three integers in A such that the sum is closest to a given number B.
Return the sum of those three integers.

Assume that there will only be one solution.
"""


def threeSumClosest(A, B):
    n = len(A)
    if n <= 3:
        return sum(A)
    A.sort()
    ref_val = A[0] + A[1] + A[2]
    for i in range(n - 2):
        j, k = i + 1, n - 1
        while j < k:
            val = A[i] + A[j] + A[k]
            if val == B:
                return val
            elif val > B:
                k -= 1
            else:
                j += 1
            if abs(val - B) < abs(ref_val - B):
                ref_val = val
    return ref_val
