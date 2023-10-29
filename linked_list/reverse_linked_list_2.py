"""
Reverse a linked list A from position B to C.
NOTE: Do it in-place and in one-pass.

1 <= |A| <= 10^6
1 <= B <= C <= |A|

Example Input

Input 1:
 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 2
 C = 4
Input 2:
 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 1
 C = 5

Example Output

Output 1:
 1 -> 4 -> 3 -> 2 -> 5
Output 2:
 5 -> 4 -> 3 -> 2 -> 1
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(left, right):
    prev, curr, next = None, left, left.next

    while prev is not right:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return next


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        dummy = ListNode(0)

        dummy.next = A
        prev, left, right = dummy, A, A

        for _ in range(B - 1):
            left = left.next
            prev = prev.next
        for _ in range(C - 1):
            right = right.next

        next = reverse_list(left, right)
        prev.next = right
        left.next = next

        return dummy.next
