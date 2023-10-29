"""
Given a binary search tree.
Return the distance between two nodes with given two keys B and C.
It may be assumed that both keys exist in BST.

NOTE: Distance between two nodes is number of edges between them.

Input 1:

         5
       /   \
      2     8
     / \   / \
    1   4 6   11
 B = 2
 C = 11
Input 2:

         6
       /   \
      2     9
     / \   / \
    1   4 7   10
 B = 2
 C = 6

Output 1:
 3
Output 2:
 1
"""


def rec_distance_from_root(root, num):
    if root.val == num:
        return 0

    if root.val > num:
        return 1 + rec_distance_from_root(root.left, num)

    return 1 + rec_distance_from_root(root.right, num)


def rec_distance_between(root, B, C):
    if root.val < B:
        return rec_distance_between(root.right, B, C)

    if root.val > C:
        return rec_distance_between(root.left, B, C)

    return rec_distance_from_root(root, B) + rec_distance_from_root(root, C)


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        (B, C) = (B, C) if B < C else (C, B)
        return rec_distance_between(A, B, C)
