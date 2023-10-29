"""
Given a binary tree with root node pointer A and an integer B.
A complete path is defined as a path from the root to a leaf.
The sum of all nodes on that path is defined as the sum of that path.
You have to remove (prune the tree) all nodes which
don't lie in any path with sum >= B.

Note: A node can be part of multiple paths.
So we have to delete it only in case when
all paths from it have sum less than B.
"""


def rec_helper(curr_sum, node, B):
    node.left, max_left_sum = rec_helper(curr_sum + node.val, node.left,
                                         B) if node.left else (None, 0)
    node.right, max_right_sum = rec_helper(curr_sum + node.val, node.right,
                                           B) if node.right else (None, 0)

    if max_left_sum + curr_sum + node.val >= B or \
            max_right_sum + curr_sum + node.val >= B:
        return node, node.val + max(max_left_sum, max_right_sum)
    else:
        return None, node.val + max(max_left_sum, max_right_sum)


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def solve(self, A, B):
        root, _ = rec_helper(0, A, B)
        return root
