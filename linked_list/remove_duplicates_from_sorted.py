"""
Given a sorted linked list, delete all duplicates such that
each element appear only once.

0 <= length of linked list <= 10^6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param A : head node of linked list
# @return the head node in the linked list
def deleteDuplicates(self, A):
    curr = A
    while curr is not None:
        last = curr
        while last.next is not None and last.next.val == curr.val:
            last = last.next
        curr.next = last.next
        curr = curr.next
    return A
