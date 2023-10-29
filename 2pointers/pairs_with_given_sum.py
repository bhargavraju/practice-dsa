"""
Given a sorted array of distinct integers A and an integer B, find and return how many pair of integers ( A[i], A[j] )
such that i != j have sum equal to B.

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the number of pairs for which sum is equal to B.
"""


def solve(A, B):
    n = len(A)
    left, right = 0, n - 1
    pairs = 0
    while left < right:
        if A[left] + A[right] > B:
            right -= 1
        elif A[left] + A[right] < B:
            left += 1
        else:
            if A[left] == A[right]:
                pairs += ((right - left) * (right - left + 1)) // 2
                break
            else:
                x, y = left, right
                while A[left] == A[x]:
                    x += 1
                while A[right] == A[y]:
                    y -= 1
                pairs += (x - left) * (right - y)
                left, right = x, y
    return pairs
