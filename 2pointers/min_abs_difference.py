"""
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that
a, b, c belongs arrays A, B, C respectively. i.e. minimize | max(a,b,c) - min(a,b,c) |.
"""


def solve(A, B, C):
    l, m, n = len(A), len(B), len(C)
    i, j, k = 0, 0, 0
    res = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))
    while i < l and j < m and k < n:
        ma = max(A[i], B[j], C[k])
        mi = min(A[i], B[j], C[k])
        res = min(res, abs(ma - mi))
        if A[i] == mi:
            i += 1
        elif B[j] == mi:
            j += 1
        else:
            k += 1
    return res
