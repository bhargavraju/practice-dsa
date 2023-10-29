"""
Given an array A of N distinct and positive elements, the task is to find number of unordered pairs whose sum
already exists in given array.

Expected Complexity : n^2

CONSTRAINTS
1 <= N <= 1000
1 <= A[i] <= 10^6 + 5
"""


# @param A : list of integers
# @return an integer
def solve(A):
    n = len(A)
    num_set = set(A)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] + A[j] in num_set:
                count += 1
    return count
