"""
Given a Binary Tree A consisting of N integer nodes, you need to find the diameter of the tree.

The diameter of a tree is the number of edges on the longest path between two nodes in the tree.
"""


# @param A : root node of tree
# @return an integer
def solve(A):
    def rec_helper(root):
        if root is None:
            return 0, 0

        left_diameter, left_height = rec_helper(root.left)
        right_diameter, right_height = rec_helper(root.right)
        curr_height = max(left_height, right_height) + 1
        curr_diameter = left_height + right_height
        return max(curr_diameter, left_diameter, right_diameter), curr_height

    diameter, _ = rec_helper(A)
    return diameter
