"""
Given a singly linked list A
 A: A0 → A1 → … → An-1 → An
reorder it to:
 A0 → An → A1 → An-1 → A2 → An-2 → …
You must do this in-place without altering the nodes' values.

Problem Constraints
1 <= |A| <= 10^6
"""


# @param A : head node of linked list
# @return the head node in the linked list
def reorderList(A):
    slow, fast = A, A
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    def reverse(head):
        prev, curr = None, head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    left, right = A, reverse(slow)
    while left is not right and left.next is not right:
        left_next = left.next
        right_next = right.next
        left.next = right
        right.next = left_next
        left = left_next
        right = right_next

    return A
