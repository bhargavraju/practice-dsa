"""
Given a binary search tree of integers. You are given a range B and C.

Return the count of the number of nodes that lies in the given range.
"""


def rec_helper(node, L, R):
    if node is None:
        return 0

    if node.val < L:
        return rec_helper(node.right, L, R)

    if node.val > R:
        return rec_helper(node.left, L, R)

    left_sum = rec_helper(node.left, L, R)
    right_sum = rec_helper(node.right, L, R)

    return 1 + left_sum + right_sum


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return rec_helper(A, B, C)
