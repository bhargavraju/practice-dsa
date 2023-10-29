"""
Given an unsorted integer array A of size N.
Find the length of the longest set of consecutive elements from the array A.

Problem Constraints
1 <= N <= 10^6
-10^6 <= A[i] <= 10^6
"""


# @param A : tuple of integers
# @return an integer
def longestConsecutive(A):
    max_len = 0
    my_set = set()
    for num in A:
        my_set.add(num)

    for num in A:
        if num - 1 in my_set:
            continue
        count = 1
        i = num
        while i + 1 in my_set:
            count += 1
            i += 1
        max_len = max(count, max_len)

    return max_len
