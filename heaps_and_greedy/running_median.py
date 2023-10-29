"""
Given an array of integers A denoting a stream of integers. New arrays of
integer B and C are formed. Each time an integer is encountered in a stream,
append it at the end of B and append median of array B at the C.

Find and return the array C.

NOTE:
If the number of elements are N in B and N is odd then consider median as
B[N/2] ( B must be in sorted order).
If the number of elements are N in B and N is even then consider median as
B[N/2-1]. ( B must be in sorted order).

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9
"""

import heapq


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        max_heap = []
        min_heap = []
        res = []
        for num in A:
            if not max_heap:
                max_heap.append(-num)
            elif not min_heap:
                first_value = -max_heap[0]
                max_heap[0] = -min(first_value, num)
                min_heap.append(max(first_value, num))
            else:
                max_val = -max_heap[0]
                min_val = min_heap[0]
                if num > min_val:
                    heapq.heappush(min_heap, num)
                else:
                    heapq.heappush(max_heap, -num)

            if len(min_heap) > len(max_heap):
                min_val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -min_val)
            elif len(max_heap) > len(min_heap) + 1:
                max_val = heapq.heappop(max_heap)
                heapq.heappush(min_heap, -max_val)

            res.append(-max_heap[0])

        return res
