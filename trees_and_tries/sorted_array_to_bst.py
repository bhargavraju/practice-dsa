"""
Given an array where elements are sorted in ascending order, convert it to a height Balanced Binary Search Tree (BBST).

Balanced tree : a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @param A : tuple of integers
# @return the root node in the tree


def sortedArrayToBST(A):
    n = len(A)
    if n == 0:
        return None
    root = TreeNode(A[n // 2])
    if n == 1:
        return root

    root.left = sortedArrayToBST(A[:n // 2])
    root.right = sortedArrayToBST(A[n // 2 + 1:])

    return root
