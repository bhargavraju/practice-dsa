"""
Find the lowest common ancestor in an unordered binary tree A given two values B and C in the tree.

Lowest common ancestor : the lowest common ancestor (LCA) of two nodes and w in a tree or directed acyclic graph (DAG)
is the lowest (i.e. deepest) node that has both v and w as descendants.

1 <= size of tree <= 100000
1 <= B, C <= 10^9
"""


# @param A : root node of tree
# @param B : integer
# @param C : integer
# @return an integer
def lca(A, B, C):
    def rec_helper(root, B, C):
        if root is None:
            return -1, False
        left_lca, left_bool = rec_helper(root.left, B, C)
        right_lca, right_bool = rec_helper(root.right, B, C)
        if root.val == B and root.val == C:
            return root.val, True
        if root.val == B or root.val == C:
            if left_lca != -1 or right_lca != -1:
                return root.val, True
            return root.val, False
        if left_lca != -1 and right_lca != -1:
            return root.val, True
        if left_lca != -1:
            return left_lca, left_bool
        if right_lca != -1:
            return right_lca, right_bool
        return -1, False

    lca_val, found = rec_helper(A, B, C)
    if found:
        return lca_val
    else:
        return -1
