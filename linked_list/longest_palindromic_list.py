"""
Given a linked list of integers. Find and return the length of the longest palindrome list
that exists in that linked list. A palindrome list is a list that reads the same backward and forward.

Expected memory complexity : O(1)

Problem Constraints
1 <= length of the linked list <= 2000
1 <= Node value <= 100

Solution explanation:
reverse the left side as you traverse along the list
divide at either nodes (or) gap between two nodes
check the lengths that are equal
"""


# @param A : head node of linked list
# @return an integer
def solve(A):
    def max_equal_length(left, right):
        count = 0
        while left is not None and right is not None:
            if left.val == right.val:
                count += 1
                left, right = left.next, right.next
            else:
                break
        return count

    curr = A
    prev = None
    max_length = 0
    while curr is not None:
        next = curr.next
        curr.next = prev
        max_length = max(max_length, 2 * max_equal_length(curr, next))
        max_length = max(max_length, 2 * max_equal_length(prev, next) + 1)
        prev = curr
        curr = next
    return max_length
