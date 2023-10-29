"""
Given a binary tree. Given a binary tree, return the values of its boundary in
anti-clockwise direction starting from the root.
Boundary includes left boundary, leaves, and right boundary in order
without duplicate nodes.

Left boundary is defined as the path from the root to the left-most node.
Right boundary is defined as the path from the root to the right-most node.
If the root doesn't have left subtree or right subtree, then the root itself
is left boundary or right boundary.
Note this definition only applies to the input binary tree,
and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you
always firstly travel to the left subtree if exists. If not,
travel to the right subtree. Repeat until you reach a leaf node. The
right-most node is also defined by the same way with left and right exchanged.

Return an array of integers denoting the boundary values of tree in
anti-clockwise order.

Input 1:
               _____1_____
              /           \
             2             3
            / \            /
           4   5          6
              / \        / \
             7   8      9  10
Output 1:
    [1, 2, 4, 7, 8, 9, 10, 6, 3]
    Explanation 1:
        The left boundary are node 1,2,4. (4 is the left-most node according to definition)
        The leaves are node 4,7,8,9,10.
        The right boundary are node 1,3,6,10. (10 is the right-most node).
        So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].

Input 2:
                1
               / \
              2   3
             / \  / \
            4   5 6  7
Output 2:
     [1, 2, 4, 5, 6, 7, 3]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rec_right(node, right_side):
    # Make sure node is not None or a leaf node
    if node is None or (node.left is None and node.right is None):
        return

    right_side.append(node.val)
    # Check example1 to understand why we check left if no right is present
    if node.right:
        rec_right(node.right, right_side)
    elif node.left:
        rec_right(node.left, right_side)


def rec_leaves(node, leaves):
    if node is None:
        return

    if node.left is None and node.right is None:
        leaves.append(node.val)
        return

    # Check left first and then right to maintain correct order
    if node.left:
        rec_leaves(node.left, leaves)
    if node.right:
        rec_leaves(node.right, leaves)


def rec_left(node, left_side):
    # Make sure node is not None or a leaf node
    if node is None or (node.left is None and node.right is None):
        return

    left_side.append(node.val)
    # We check right if no left present, same reason as rec_right
    if node.left:
        rec_left(node.left, left_side)
    elif node.right:
        rec_left(node.right, left_side)


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        if A is None:
            return []

        left_side = []
        rec_left(A.left, left_side)

        leaves = []
        rec_leaves(A.left, leaves)
        rec_leaves(A.right, leaves)

        right_side = []
        rec_right(A.right, right_side)

        return [A.val] + left_side + leaves + right_side[::-1]
