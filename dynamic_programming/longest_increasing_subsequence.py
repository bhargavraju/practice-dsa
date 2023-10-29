"""
Find the longest increasing subsequence of a given array of integers, A.

In other words, find a subsequence of array in which the subsequence's
 elements are in strictly increasing order, and in which the subsequence is
 as long as possible.

In this case, return the length of the longest increasing subsequence.

Problem Constraints
0 <= length(A) <= 2500
1 <= A[i] <= 2500
"""


# @param A : tuple of integers
# @return an integer
def lis(A):
    n = len(A)
    max_length = [1]*(n+1)
    max_length[0] = 0
    for i in range(2, n+1):
        for j in range(1, i):
            if A[j-1] < A[i-1]:
                max_length[i] = max(max_length[j] + 1, max_length[i])
    return max(max_length)
