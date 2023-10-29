"""
Consider lines of slope -1 passing between nodes.

Given a Binary Tree A containing N nodes,
return all diagonal elements in a binary tree belonging to same line.

Input 1:

            1
          /   \
         4      2
        / \      \
       8   5      3
          / \    /
         9   7  6
Input 2:

             11
          /     \
         20      12
        / \       \
       1   15      13
          /  \     /
         2    17  16
          \   /
          22 34

Output 1:
 [1, 2, 3, 4, 5, 7, 6, 8, 9]
Output 2:
 [11, 12, 13, 20, 15, 17, 16, 1, 2, 22, 34]
"""

from collections import defaultdict


def rec_helper(root, level, res):
    if root is None:
        return
    res[level].append(root.val)
    if root.left:
        rec_helper(root.left, level + 1, res)
    if root.right:
        rec_helper(root.right, level, res)


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        res = defaultdict(list)
        rec_helper(A, 0, res)
        ans = []

        i = 0
        while i in res:
            ans += res[i]
            i += 1

        return ans
