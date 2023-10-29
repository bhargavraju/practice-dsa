"""
Given a complete binary tree, A, find the total number of nodes in the tree.

A Binary Tree is a Complete Binary Tree if
all the levels are completely filled except possibly the last level and
the last level has all keys as left as possible

               18
           /       \
         15         30
        /  \        /  \
      40    50    100   40

               18
           /       \
         15         30
        /  \        /  \
      40    50    100   40
     /  \   /
    8   7  9
"""


def is_present(no, h, root):
    if h < 2:
        return True

    ptr = root
    set_no = 1 << (h - 2)
    while set_no:
        if set_no & (no - 1):
            ptr = ptr.right
        else:
            ptr = ptr.left

        set_no = set_no >> 1

    if ptr is None:
        return False

    return True


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        h = 0
        ptr = A

        while ptr:
            ptr = ptr.left
            h += 1

        l, r = 1, pow(2, h - 1)
        nodes_in_last = 1

        while l <= r:
            mid = (l + r) // 2
            if is_present(mid, h, A):
                nodes_in_last = mid
                l = mid + 1
            else:
                r = mid - 1

        return pow(2, h - 1) - 1 + nodes_in_last