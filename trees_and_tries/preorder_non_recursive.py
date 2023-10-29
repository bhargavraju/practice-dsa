"""
Given a binary tree, return the preorder traversal of its nodes values.

NOTE: Using recursion is not allowed.
"""

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        res = []
        if A is None:
            return res
        queue = deque([A])

        while queue:
            el = queue.popleft()
            if el.right is not None:
                queue.appendleft(el.right)
            if el.left is not None:
                queue.appendleft(el.left)
            res.append(el.val)

        return res
