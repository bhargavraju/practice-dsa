"""
Given a binary tree,
return the zigzag level order traversal of its nodes values.
(ie, from left to right, then right to left for the next level and
alternate between).
"""

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        res = []
        queue = deque([A])
        reverse = False

        while queue:
            curr_level = deque()
            level_len = len(queue)

            for _ in range(level_len):
                el = queue.popleft()
                if el.left is not None:
                    queue.append(el.left)
                if el.right is not None:
                    queue.append(el.right)
                if reverse:
                    curr_level.appendleft(el.val)
                else:
                    curr_level.append(el.val)

            reverse = not reverse
            res.append(curr_level)

        return res
