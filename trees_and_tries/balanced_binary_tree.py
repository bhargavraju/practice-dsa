"""
Given a root of binary tree A, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node
never differ by more than 1.

Problem Constraints
1 <= size of tree <= 100000

Input Format
First and only argument is the root of the tree A.

Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
"""


# @param A : root node of tree
# @return an integer
def isBalanced(A):

    def rec_helper(node):
        if node is None:
            return -1, True
        left_height, left_is_balanced = rec_helper(node.left)
        right_height, right_is_balanced = rec_helper(node.right)

        curr_height = max(left_height, right_height) + 1

        if left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1:
            return curr_height, True
        else:
            return curr_height, False

    _, is_balanced = rec_helper(A)
    return int(is_balanced)
