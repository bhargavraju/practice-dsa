"""
Given a sorted matrix of integers A of size N x M and an integer B.
Each of the rows and columns of matrix A are sorted in ascending order,
find the Bth smallest element in the matrix.

NOTE: Return The Bth smallest element in the sorted order, not the
Bth distinct element.

Problem Constraints
1 <= N, M <= 500
1 <= A[i] <= 10^9
1 <= B <= N * M
"""

import heapq


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(A[0])

        heap = []
        for i in range(n):
            heapq.heappush(heap, (A[i][0], i, 0))

        while B - 1:
            _, i, j = heapq.heappop(heap)
            if j + 1 < m:
                heapq.heappush(heap, (A[i][j + 1], i, j + 1))
            B -= 1

        return heap[0][0]
