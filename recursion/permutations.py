"""
Given an integer array A of size N denoting collection of numbers , return all possible permutations.

NOTE:
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
"""


# @param A : list of integers
# @return a list of list of integers
def permute(A):
    n = len(A)
    A.sort()
    perms = []

    def recurse(arr, curr, res):
        if len(arr) == 1:
            res.append(curr + arr)
            return
        i = 0
        while i < len(arr):
            recurse(arr[:i] + arr[i + 1:], curr + [arr[i]], res)
            i += 1

    recurse(A, [], perms)
    return perms
