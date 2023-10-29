"""
Given a binary tree
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

 Note:
You may only use constant extra space.
"""


def get_next_node(node):
    next_node = node.next

    while next_node:
        if next_node.left:
            return next_node.left
        elif next_node.right:
            return next_node.right

        next_node = next_node.next


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        start_node = root

        while start_node:
            curr_level_start_node = start_node
            curr = start_node
            while curr:
                if curr.left:
                    if start_node is curr_level_start_node:
                        start_node = curr.left

                    if curr.right:
                        curr.left.next = curr.right
                    else:
                        curr.left.next = get_next_node(curr)
                if curr.right:
                    if start_node is curr_level_start_node:
                        start_node = curr.right

                    curr.right.next = get_next_node(curr)

                curr = curr.next

            if start_node is curr_level_start_node:
                start_node = None
