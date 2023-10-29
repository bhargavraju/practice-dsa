"""
Given a binary tree, return the inorder traversal of its nodes values.

NOTE: Using recursion is not allowed.
"""


def inorderTraversal(A):
    res = []
    st = []
    node = A

    while len(st) > 0 or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()
            res.append(node.val)
            node = node.right
    return res
