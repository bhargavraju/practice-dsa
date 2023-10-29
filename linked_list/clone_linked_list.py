"""
Given a doubly linked list of integers with one pointer of each node pointing to the next node (just like in a
single link list) while the second pointer, however, can point to any node in the list and not just the previous node.

You have to create a copy of this list and return the head pointer of the duplicated list.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


def clonelist(A):
    map = {}
    curr = A
    new_list = ListNode(0)
    prev = new_list
    while curr is not None:
        new_node = ListNode(curr.val)
        prev.next = new_node
        map[curr] = new_node
        curr = curr.next
        prev = new_node
    prev.next = None
    start = new_list.next
    curr = A
    while curr is not None:
        start.random = map[curr.random]
        curr = curr.next
        start = start.next
    return new_list.next
