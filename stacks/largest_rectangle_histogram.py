"""
Given an array of integers A . A represents a histogram i.e A[i] denotes height of the ith histogram's bar.
Width of each bar is 1. Find the area of the largest rectangle formed by the histogram.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 1000000000
"""


# @param A : list of integers
# @return an integer
def largestRectangleArea(A):
    n = len(A)

    left_st = []
    left_min = [-1] * n
    for i in range(n):
        el = A[i]
        while len(left_st) > 0 and A[left_st[-1]] >= el:
            left_st.pop()
        if len(left_st) > 0:
            left_min[i] = left_st[-1]
        left_st.append(i)

    right_st = []
    right_min = [n] * n
    for i in range(n - 1, -1, -1):
        el = A[i]
        while len(right_st) > 0 and A[right_st[-1]] >= el:
            right_st.pop()
        if len(right_st) > 0:
            right_min[i] = right_st[-1]
        right_st.append(i)

    max_area = float('-inf')
    for i in range(n):
        max_area = max(max_area, A[i] * (right_min[i] - left_min[i] - 1))
    return max_area
