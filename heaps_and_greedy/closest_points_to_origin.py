"""
We have a list A, of points(x,y) on the plane. Find the B closest points to
the origin (0, 0). Here, the distance between two points on a plane is the
Euclidean distance. You may return the answer in any order. The answer is
guaranteed to be unique (except for the order that it is in.)

NOTE: Euclidean distance between two points P1(x1,y1) and P2(x2,y2) is
 sqrt( (x1-x2)2 + (y1-y2)2 ).


Problem Constraints
1 <= B <= length of the list A <= 100000
-100000 <= A[i][0] <= 100000
-100000 <= A[i][1] <= 100000
"""

import heapq


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        arr = [(p[0]*p[0] + p[1]*p[1], p) for p in A]
        heapq.heapify(arr)
        ans = []
        for i in range(B):
            distance, point = heapq.heappop(arr)
            ans.append(point)
        return ans
