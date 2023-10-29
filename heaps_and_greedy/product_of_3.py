"""
Given an integer array A of size N. You have to find the product of
the 3 largest integers in array A from range 1 to i, where i goes from 1 to N.

Return an array B where B[i] is the product of the largest 3 integers in
range 1 to i in array A. If i < 3, then the integer at index i is -1.

Problem Constraints
1 <= N <= 10^5
0 <= A[i] <= 10^3
"""

import heapq


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        heap = []
        ans = []
        for i in range(len(A)):
            heapq.heappush(heap, -A[i])
            if i < 2:
                ans.append(-1)
                continue
            first, second, third = heapq.heappop(heap), heapq.heappop(heap), heapq.heappop(heap)
            product = (-first)*(-second)*(-third)
            ans.append(product)
            heapq.heappush(heap, first)
            heapq.heappush(heap, second)
            heapq.heappush(heap, third)
        return ans
