"""
Given a linked list A, remove the B-th node from the end of list and return its head.
For example, Given linked list: 1->2->3->4->5, and B = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

NOTE: If B is greater than the size of the list, remove the first node of the list.
NOTE: Try doing it using constant additional space.
"""


# @param A : head node of linked list
# @param B : integer
# @return the head node in the linked list
def removeNthFromEnd(A, B):
    if A is None or B <= 0:
        return A
    right = A
    for i in range(B):
        if right.next is None:
            return A.next
        right = right.next
    left = A
    while right.next is not None:
        left = left.next
        right = right.next
    left.next = left.next.next
    return A
