"""
Given two integers arrays A and B of size N each. Find the maximum N elements
from the sum combinations (Ai + Bj) formed from elements in array A and B.


Problem Constraints
1 <= N <= 2 * 10^5
-1000 <= A[i], B[i] <= 1000


Input Format
First argument is an integer array A.
Second argument is an integer array B.


Output Format
Return an intger array denoting the N maximum element in descending order.


Example Input
Input 1:
 A = [1, 4, 2, 3]
 B = [2, 5, 1, 6]
Input 2:
 A = [2, 4, 1, 1]
 B = [-2, -3, 2, 4]


Example Output
Output 1:
 [10, 9, 9, 8]
Output 2:
 [8, 6, 6, 5]
"""


import heapq


# @param A : list of integers
# @param B : list of integers
# @return a list of integers
def solve(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    n = len(A)
    heap = [(-A[0] - B[j], 0, j) for j in range(n)]
    heapq.heapify(heap)
    ans = []
    for _ in range(n):
        val, i, j = heapq.heappop(heap)
        ans.append(-val)
        if i+1 < n:
            heapq.heappush(heap, (-A[i+1] - B[j], i+1, j))
    return ans
