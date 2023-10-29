"""
Merge two sorted linked lists A and B and return it as a new list.
The new list should be made by splicing together
the nodes of the first two lists, and should also be sorted.

Example Input

Input 1:
 A = 5 -> 8 -> 20
 B = 4 -> 11 -> 15
Input 2:
 A = 1 -> 2 -> 3
 B = Null

Example Output

Output 1:
 4 -> 5 -> 8 -> 11 -> 15 -> 20
Output 2:
 1 -> 2 -> 3
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param A : head node of linked list
# @param B : head node of linked list
# @return the head node in the linked list
def mergeTwoLists(self, A, B):
    dummy = ListNode(0)
    curr = dummy
    while A is not None and B is not None:
        if A.val < B.val:
            curr.next = A
            A = A.next
        else:
            curr.next = B
            B = B.next
        curr = curr.next

    if A is None:
        curr.next = B
    if B is None:
        curr.next = A

    return dummy.next
