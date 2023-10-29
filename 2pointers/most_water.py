"""
Given n non-negative integers A[0], A[1], ..., A[n-1] , where each represents a point at coordinate (i, A[i]).
N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container.

Problem Constraints
0 <= N <= 105
1 <= A[i] <= 105

Input Format
Single Argument representing a 1-D array A.

Output Format
Return single Integer denoting the maximum area you can obtain.
"""


def maxArea(A):
    n = len(A)
    left, right = 0, n - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(A[left], A[right]) * (right - left))
        if A[left] == min(A[left], A[right]):
            left += 1
        else:
            right -= 1
    return max_area
