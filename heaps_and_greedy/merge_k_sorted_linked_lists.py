"""
Given a list containing head pointers of N sorted linked lists.
Merge these N given sorted linked lists and return it as one sorted list.


Problem Constraints
1 <= total number of elements in given linked lists <= 100000


Input Format
First and only argument is a list containing N head pointers.


Output Format
Return a pointer to the head of the sorted linked list after merging all the
given linked lists.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class CustomListNode:

    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        heap = [CustomListNode(node.val, node.next) for node in A]
        heapq.heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap:
            min_node = heapq.heappop(heap)
            node = ListNode(min_node.val)
            curr.next = node
            curr = node
            if min_node.next:
                next_node = CustomListNode(min_node.next.val, min_node.next.next)
                heapq.heappush(heap, next_node)
        return dummy.next
