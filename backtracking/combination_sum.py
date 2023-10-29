"""
Given a set of candidate numbers A and a target number B, find all unique combinations in A where
the candidate numbers sums to B. The same repeated number may be chosen from A unlimited number of times.

Note:
1) All numbers (including target) will be positive integers.
2) Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
3) The combinations themselves must be sorted in ascending order.
4) CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR ...
    (a1 = b1 AND a2 = b2 AND ... ai = bi AND ai+1 > bi+1)
5) The solution set must not contain duplicate combinations.
"""


# @param A : list of integers
# @param B : integer
# @return a list of list of integers
def combinationSum(A, B):
    A.sort()

    def rec_helper(arr, curr_list, curr_sum, res):
        if curr_sum == B:
            res.append(curr_list)
            return
        if curr_sum > B:
            return
        if len(arr) == 0:
            return

        j = 0
        while j < len(arr) and arr[0] == arr[j]:
            j += 1
        rec_helper(arr, curr_list + [arr[0]], curr_sum + arr[0], res)
        rec_helper(arr[j:], curr_list, curr_sum, res)

    ans = []
    rec_helper(A, [], 0, ans)
    return ans
