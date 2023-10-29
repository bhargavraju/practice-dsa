"""
Given N persons with different priorities standing in a queue. Queue is
following a property that Each person is standing at most B places away from
it's sorted position.

Your task is to sort the queue in the increasing order of priorities.

NOTE:
No two persons can have the same priority.
Use the property of the queue to sort the queue with complexity O(NlogB).

Problem Constraints
1 <= N <= 100000
0 <= B < N
"""


import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        if B == 0:
            return A
        heap = A[:B+1]
        heapq.heapify(heap)
        n = len(A)
        for i in range(n):
            val = heapq.heappop(heap)
            if i+B+1 < n:
                heapq.heappush(heap, A[i+B+1])
            A[i] = val
        return A
