"""
Given a binary tree, return the Postorder traversal of its nodes values.

NOTE: Using recursion is not allowed.
"""


# @param A : root node of tree
# @return a list of integers
def postorderTraversal(A):
    curr = A
    prev = None
    st = []
    ans = []
    while len(st) > 0 or curr is not None:
        if curr is not None:
            st.append(curr)
            curr = curr.left
        else:
            curr = st[-1]
            if curr.right is None or curr.right == prev:
                ans.append(curr.val)
                st.pop()
                prev = curr
                curr = None
            else:
                curr = curr.right
    return ans
