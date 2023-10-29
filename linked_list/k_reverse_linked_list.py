"""
Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and
return modified linked list.

Problem Constraints
1 <= |A| <= 10^3

B always divides A
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param A : head node of linked list
# @param B : integer
# @return the head node in the linked list
def reverseList(A, B):
    def reverse(start, end):
        prev, curr = None, start
        while prev is not end:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return start, prev, curr

    node = ListNode(0)
    node.next = A
    prev = node
    left = A
    while left is not None:
        right = left
        for _ in range(B - 1):
            right = right.next
        rev_left, rev_right, new_left = reverse(left, right)
        prev.next = rev_right
        rev_left.next = new_left
        prev = rev_left
        left = new_left
    return node.next
