"""
Given an array of integers A, find and return whether the given array contains a non-empty sub array with a
sum equal to 0. If the given array contains a sub-array with sum zero return 1 else return 0.

Problem Constraints
1 <= |A| <= 100000
-10^9 <= A[i] <= 10^9

Solution explanation: Initialized sum index map with {0: -1} to accommodate cases where the sub array starts with the
first element
"""


# @param A : list of integers
# @return an integer
def solve(A):
    n = len(A)
    prefix_sum = [A[0]] * n
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]

    sum_index_map = {0: -1}
    for i in range(n):
        pref_sum = prefix_sum[i]
        if pref_sum in sum_index_map:
            return 1
        else:
            sum_index_map[pref_sum] = i

    return 0
