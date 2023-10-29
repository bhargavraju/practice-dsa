"""
You are given a binary tree.
Find all paths from root to leaves of the binary tree.
"""


def rec_helper(node, curr, res):
    if node.left is None and node.right is None:
        res.append(curr + [node.val])
        return

    if node.left:
        rec_helper(node.left, curr + [node.val], res)

    if node.right:
        rec_helper(node.right, curr + [node.val], res)


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def solve(self, A):
        res = []
        rec_helper(A, [], res)
        return res
