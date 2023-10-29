"""
Given preorder and inorder traversal of a tree, construct the binary tree.

NOTE: You may assume that duplicates do not exist in the tree.

Input Format
First argument is an integer array A denoting the preorder traversal of the tree.
Second argument is an integer array B denoting the inorder traversal of the tree.

Output Format
Return the root node of the binary tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    pre_index = 0

    def search(self, val, in_order, start, end):
        for i in range(start, end + 1):
            if val == in_order[i]:
                return i

    def build_tree(self, pre_order, in_order, in_start, in_end):
        """
        Since the recursion of this function follows pre-order, we follow the
        same order as the pre-order array and get the corresponding values to
        build nodes
        """
        if in_start > in_end:
            return None

        node = TreeNode(pre_order[self.pre_index])
        self.pre_index += 1

        in_index = self.search(node.val, in_order, in_start, in_end)

        node.left = self.build_tree(pre_order, in_order, in_start,
                                    in_index - 1)
        node.right = self.build_tree(pre_order, in_order, in_index + 1, in_end)

        return node

    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        return self.build_tree(A, B, 0, len(B) - 1)
