"""
Given a linked list of integers.
Find and return the middle element of the linked list.

NOTE: If there are N nodes in the linked list and N is even then
return the (N/2 + 1)th element.

1 <= length of the linked list <= 100000
1 <= Node value <= 10^9
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        slow, fast = A, A

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        if fast.next is None:
            return slow.val

        if fast.next.next is None:
            return slow.next.val
