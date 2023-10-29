"""
Given an array 'A' of sorted integers and another non negative integer k,
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

 Example: Input :
    A : [1 3 5]
    k : 4
 Output : YES as 5 - 1 = 4
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Try doing this in less than linear space complexity.
"""


def diffPossible(A, B):
    n = len(A)
    if n < 2:
        return 0
    i, j = 0, 1
    while i < n and j < n:
        if i == j:
            j += 1
            continue
        if abs(A[i] - A[j]) == B:
            return 1
        elif abs(A[i] - A[j]) < B:
            j += 1
        else:
            i += 1
    return 0
