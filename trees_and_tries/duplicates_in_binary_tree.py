"""
Given a binary tree of integers, return whether it contains a duplicate
sub-tree of size 2 or more. All node values lie between 0 and 9 inclusive.

Return 1 if it contains a duplicate sub-tree of size 2 or more else return 0.

Note: Two same leaf nodes are not considered as a subtree,
As the size of a leaf node is one.
"""


def rec_helper(trees, node):
    if node is None:
        return '$', False

    left_tree, left_present = rec_helper(trees, node.left)
    right_tree, right_present = rec_helper(trees, node.right)

    curr_tree = str(node.val) + left_tree + right_tree

    if left_present or right_present:
        return curr_tree, True

    if len(curr_tree) > 3 and curr_tree in trees:
        return curr_tree, True

    trees.add(curr_tree)
    return curr_tree, False


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        trees = set()
        _, is_present = rec_helper(trees, A)
        return int(is_present)
