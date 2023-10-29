"""
Given two integers A and B, return all possible combinations of B numbers out of 1 2 3 ... A .
Make sure the combinations are sorted.

To elaborate,
Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.

Input 1:
 A = 4
 B = 2

Output 1:
[
  [1, 2],
  [1, 3],
  [1, 4],
  [2, 3],
  [2, 4],
  [3, 4],
 ]
"""


# @param A : integer
# @param B : integer
# @return a list of list of integers
def combine(A, B):
    arr = [i for i in range(1, A + 1)]

    def rec_helper(arr, count, curr, res):
        if count == 0:
            res.append(curr)
            return

        i = 0
        while i < len(arr):
            rec_helper(arr[i + 1:], count - 1, curr + [arr[i]], res)
            i += 1

    ans = []
    rec_helper(arr, B, [], ans)
    return ans
