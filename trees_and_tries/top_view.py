"""
Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the
Binary tree. Right view of a Binary Tree is a set of nodes visible when the tree is visited from top.

Return the nodes in any order.
"""


# @param A : root node of tree
# @return a list of integers
def solve(A):
    dist_dict = {}
    queue = [(A, 0)]

    while queue:
        level_length = len(queue)
        first, last = queue[0], queue[-1]
        if first[1] not in dist_dict:
            dist_dict[first[1]] = first[0].val
        if last[1] not in dist_dict:
            dist_dict[last[1]] = last[0].val

        for i in range(level_length):
            node, dist = queue.pop(0)
            if node.left is not None:
                queue.append((node.left, dist - 1))
            if node.right is not None:
                queue.append((node.right, dist + 1))

    return list(dist_dict.values())
