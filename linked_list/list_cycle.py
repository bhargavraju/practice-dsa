"""
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.
Try solving it using constant additional space.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param A : head node of linked list
# @return the head node in the linked list
def detectCycle(self, A):
    slow, fast = A, A
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            slow = A
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow
