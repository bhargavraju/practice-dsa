"""
Given two BST's A and B, return the
(sum of all common nodes in both A and B) % (10^9 +7) .

In case there is no common node, return 0.
"""

from collections import deque


def add_node_and_left_successors(st, node):
    st.append(node)
    left_child = node.left

    while left_child:
        st.append(left_child)
        left_child = left_child.left


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def solve(self, A, B):
        st_a = deque()
        st_b = deque()

        add_node_and_left_successors(st_a, A)
        add_node_and_left_successors(st_b, B)

        res = []

        while st_a and st_b:

            if st_a[-1].val == st_b[-1].val:
                res.append(st_a[-1].val)
                a_top = st_a.pop()
                b_top = st_b.pop()
                if a_top.right:
                    add_node_and_left_successors(st_a, a_top.right)
                if b_top.right:
                    add_node_and_left_successors(st_b, b_top.right)

            elif st_a[-1].val < st_b[-1].val:
                a_top = st_a.pop()
                if a_top.right:
                    add_node_and_left_successors(st_a, a_top.right)

            else:
                b_top = st_b.pop()
                if b_top.right:
                    add_node_and_left_successors(st_b, b_top.right)

        return sum(res) % 1000000007
