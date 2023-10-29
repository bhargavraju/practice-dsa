"""
Given a set of distinct integers, A, return all possible subsets.

NOTE:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.

A = [1, 2, 3]
[
 []
 [1]
 [1, 2]
 [1, 2, 3]
 [1, 3]
 [2]
 [2, 3]
 [3]
]
"""


# @param A : list of integers
# @return a list of list of integers
def subsets(A):
    n = len(A)
    A.sort()

    def rec_helper(arr):
        if len(arr) == 0:
            return [[]]
        remaining = rec_helper(arr[1:])
        curr = [[arr[0]] + comb for comb in remaining]
        curr.extend(remaining)
        return curr

    res = rec_helper(A)
    res.sort()
    return res
