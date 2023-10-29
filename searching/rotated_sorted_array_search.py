"""
Given a sorted array of integers A of size N and an integer B.
array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, otherwise return -1.
You may assume no duplicate exists in the array.

NOTE: Users are expected to solve this in O(log(N)) time.

Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 10^9

all elements in A are distinct.
"""


# @param A : tuple of integers
# @param B : integer
# @return an integer
def search(A, B):
    n = len(A)

    def find_pivot():
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if mid < n - 1 and A[mid] > A[mid + 1]:
                return mid + 1
            elif A[left] <= A[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return 0

    pivot = find_pivot()
    if B < A[pivot] or B > A[pivot - 1]:
        return -1
    l, r = 0, n - 1
    if A[pivot] <= B <= A[n - 1]:
        l = pivot
    else:
        r = pivot - 1

    while l <= r:
        m = (l + r) // 2
        if A[m] == B:
            return m
        elif A[m] > B:
            r = m - 1
        else:
            l = m + 1
    return -1
