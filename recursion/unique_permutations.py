"""
Given an array A of size N denoting collection of numbers that might contain duplicates,
return all possible unique permutations.

NOTE: No 2 entries in the permutation sequence should be the same.
"""


# @param A : list of integers
# @return a list of list of integers
def permute(A):
    A.sort()

    def rec(arr, curr, res):
        if len(arr) == 1:
            res.append(curr + arr)
            return
        i = 0
        while i < len(arr):
            rec(arr[:i] + arr[i + 1:], curr + [arr[i]], res)
            j = i
            while j < len(arr) and arr[j] == arr[i]:
                j += 1
            i = j

    perms = []
    rec(A, [], perms)
    return perms
