"""
Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and
return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
Note that even though we want you to return the new length, make sure to change the original array as well in place

For example, Given input array A = [1,1,1,2],
Your function should return length = 3, and A is now [1,1,2].
"""


def removeDuplicates(A):
    i = 0
    while i < len(A):
        j = i
        while j < len(A) and A[j] == A[i]:
            j += 1
        if j > i + 2:
            del A[i + 2:j]
            i += 2
        else:
            i = j
    return len(A)
