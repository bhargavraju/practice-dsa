"""
Given an array of integers A. If i < j and A[i] > A[j] then the pair (i, j) is called an inversion of A.
Find the total number of inversions of A modulo (10^9 + 7).

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9
"""


def solve(A):
    n = len(A)
    if n < 2:
        return 0
    mid = n // 2
    left_arr, right_arr = A[:mid], A[mid:]
    count = (solve(left_arr) + solve(right_arr)) % 1000000007
    left_arr.sort()
    right_arr.sort()
    i, j = 0, 0
    while i < len(left_arr) and j < len(right_arr):
        while i < len(left_arr) and left_arr[i] <= right_arr[j]:
            i += 1
        count = (count + len(left_arr) - i) % 1000000007
        j += 1
    return count


# 2nd (better?) solution below


def mergesort(self, A):
    n = len(A)
    if n < 2:
        return 0

    left = A[:n // 2]
    right = A[n // 2:]

    left_count = self.mergesort(left)
    right_count = self.mergesort(right)

    i, j, k = 0, 0, 0
    across_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            across_count += len(left) - i
            A[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        A[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        A[k] = right[j]
        k += 1
        j += 1

    return (across_count + left_count + right_count) % 1000000007


# @param A : list of integers
# @return an integer
def solve(self, A):
    return self.mergesort(A)
