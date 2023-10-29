"""
Given an array of integers A and an integer B. You must modify the array
exactly B number of times. In single modification, we can replace
any one array element A[i] by -A[i].

You need to perform these modifications in such a way that after
exactly B modifications, sum of the array must be maximum.


Problem Constraints
1 <= length of the array <= 5x10^5
1 <= B <= 5x10^6
-100 <= A[i] <= 100
"""


import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        heapq.heapify(A)
        for i in range(B):
            smallest = A[0]
            heapq.heapreplace(A, -1*smallest)
        return sum(A)
