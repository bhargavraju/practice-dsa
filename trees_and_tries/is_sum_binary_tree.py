"""
Given a binary tree. Check whether the given tree is a Sum-binary Tree or not.

Sum-binary Tree is a Binary Tree where the value of a every node is equal to
sum of the nodes present in its left subtree and right subtree.

An empty tree is Sum-binary Tree and sum of an empty tree can be
considered as 0. A leaf node is also considered as SumTree.

Return 1 if it sum-binary tree else return 0.
"""


def rec_helper(node):
    if node.left is None and node.right is None:
        return True, node.val

    left_is_sum_binary, left_tree_sum = rec_helper(
        node.left) if node.left else (True, 0)
    right_is_sum_binary, right_tree_sum = rec_helper(
        node.right) if node.right else (True, 0)

    if left_is_sum_binary and right_is_sum_binary:
        if node.val == left_tree_sum + right_tree_sum:
            return True, node.val + left_tree_sum + right_tree_sum

    return False, node.val + left_tree_sum + right_tree_sum


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if A is None:
            return 1

        is_sum_binary, _ = rec_helper(A)
        return int(is_sum_binary)
