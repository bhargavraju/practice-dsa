"""
Given a binary tree of integers. Return an array of integers representing the left view of the Binary tree.
Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side

NOTE: The value comes first in the array which have lower level.
"""


# @param A : root node of tree
# @return a list of integers
def solve(A):
    queue = ['$', A]
    ans = []
    while len(queue) > 0:
        top = queue.pop(0)
        if top == '$':
            if len(queue) > 0:
                ans.append(queue[0].val)
                queue.append('$')
        else:
            if top.left is not None:
                queue.append(top.left)
            if top.right is not None:
                queue.append(top.right)
    return ans
