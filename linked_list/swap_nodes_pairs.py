"""
Given a linked list A, swap every two adjacent nodes and return its head.

NOTE: Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.

Example Input

Input 1:
 A = 1 -> 2 -> 3 -> 4
Input 2:
 A = 7 -> 2 -> 1

Example Output
Output 1:
 2 -> 1 -> 4 -> 3
Output 2:
 2 -> 7 -> 1
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param A : head node of linked list
# @return the head node in the linked list
def swapPairs(self, A):
    if A is None:
        return A

    dummy = ListNode(0)
    dummy.next = A

    prev, curr = dummy, A
    while curr is not None and curr.next is not None:
        second_node = curr.next
        next = second_node.next
        second_node.next = curr
        curr.next = next
        prev.next = second_node

        prev = curr
        curr = next

    return dummy.next
