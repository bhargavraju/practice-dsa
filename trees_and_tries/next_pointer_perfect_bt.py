"""
Given a binary tree,

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Assume perfect binary tree and try to solve this in constant extra space.
"""


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        curr_level_head = root
        while curr_level_head:
            curr= curr_level_head
            curr_level_head = curr_level_head.left
            while curr:
                next = curr.next
                if curr.left and curr.right:
                    curr.left.next = curr.right
                    if next:
                        curr.right.next = next.left
                curr = next
