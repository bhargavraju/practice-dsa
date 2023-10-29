"""
Given a Binary Tree A with N nodes. Write a function that returns the
size of the largest subtree which is also a Binary Search Tree (BST).

If the complete Binary Tree is BST, then return the size of whole tree.

NOTE:
Largest subtree means subtree with most number of nodes.

Problem Constraints
1 <= N <= 10^5
"""


def rec_helper(root):
    left_is_bst, left_min, left_max, left_size = rec_helper(root.left) if \
        root.left else (True, float('inf'), float('-inf'), 0)
    right_is_bst, right_min, right_max, right_size = rec_helper(root.right) if \
        root.right else (True, float('inf'), float('-inf'), 0)

    if left_is_bst and right_is_bst and left_max < root.val < right_min:
        return (
            True,
            min(left_min, root.val),
            max(right_max, root.val),
            1 + left_size + right_size
        )

    return (
        False,
        min(left_min, root.val, right_min),
        max(left_max, root.val, right_max),
        max(left_size, right_size)
    )


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        _, _, _, size = rec_helper(A)
        return size
