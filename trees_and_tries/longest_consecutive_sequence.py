"""
Given a binary tree. Find the length of the longest path which comprises of
nodes with consecutive values in increasing order.
Every node is considered as a path of length 1.

The path refers to any sequence of nodes from some starting node to any node
in the tree along the parent-child connections.

Note: The longest consecutive path need to be from parent to child
(cannot be the reverse).
"""


def rec_helper(node):
    if node.left is None and node.right is None:
        return 1, 1

    left_longest, left_longest_so_far = rec_helper(
        node.left) if node.left else (0, 0)
    right_longest, right_longest_so_far = rec_helper(
        node.right) if node.right else (0, 0)

    curr_longest = 1
    if node.left and node.left.val == node.val + 1:
        curr_longest = max(curr_longest, 1 + left_longest)
    if node.right and node.right.val == node.val + 1:
        curr_longest = max(curr_longest, 1 + right_longest)

    return curr_longest, max(curr_longest, left_longest_so_far,
                             right_longest_so_far)


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if A is None:
            return 0

        _, longest = rec_helper(A)
        return longest
