"""
Given a sorted array of distinct integers A and an integer B, find and return how many rectangles with
distinct configurations can be created using elements of this array as length and breadth whose area is lesser than B.

(Note that a rectangle of 2 x 3 is different from 3 x 2 if we take configuration into view)

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 109
1 <= B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the number of rectangles with distinct configurations with area less than B modulo (10^9 + 7).
"""


def solve(A, B):
    n = len(A)
    if n < 2:
        return 1 if A[0] * A[0] < B else 0
    count = 0
    i, j = 0, n - 1
    while i <= j:
        if A[i] * A[j] < B:
            count = (count + 2 * (j - i) + 1) % 1000000007
            i += 1
        else:
            j -= 1
    return count
