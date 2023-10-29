"""
You are given two integers A and B.
A describes the number of nodes in complete binary tree.
You are B steps away from your destination in the worst case.

Initially, you can be at:
The root node of the tree and can only move bottom of the tree.
Any leaf node of the tree and can only move up the tree.
Find and return an array of integers C of size 2 where

C[0]: The number of nodes which are at B steps from the root, i.e.
the number of nodes such that, starting at that root,
you have to take B steps downwards to reach the node.

C[1]: The number of nodes such that the maximum distance from the node to
any leaf in the subtree of the node is B.

NOTE: A Complete binary tree is a binary tree in which every level,
except possibly the last, is completely filled, and
all nodes are as far left as possible.
"""


# @param A : integer
# @param B : integer
# @return a list of integers
def solve(A, B):
    temp = A
    level = 0
    from_root = []

    while temp > 0:
        from_root.append(min(1 << level, temp))
        temp -= min(1 << level, temp)
        level += 1
    level -= 1

    from_leaf = from_root[::-1]
    missing = (1 << level) - from_leaf[0]

    i = 0
    while missing > 0:
        missing = missing >> 1
        from_leaf[i] += missing
        from_leaf[i + 1] -= missing
        i += 1

    if B > level:
        return [0, 0]

    return [from_root[B], from_leaf[B]]
