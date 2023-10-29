"""
Given a collection of integers denoted by array A of size N that might contain duplicates, return all possible subsets.

NOTE:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
"""


# @param A : list of integers
# @return a list of list of integers
def subsetsWithDup(A):
    A.sort()

    def rec_helper(arr):
        if len(arr) == 0:
            return [[]]
        j = 0
        while j < len(arr) and arr[0] == arr[j]:
            j += 1
        remaining = rec_helper(arr[j:])
        curr = []
        for subset in remaining:
            possibilities = []
            for _ in range(j):
                if possibilities:
                    possibilities.append([arr[0]] + possibilities[-1])
                else:
                    possibilities.append([arr[0]] + subset)
            curr.extend(possibilities)
        curr.extend(remaining)
        return curr

    ans = rec_helper(A)
    ans.sort()
    return ans
