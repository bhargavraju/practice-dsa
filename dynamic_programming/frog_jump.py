"""
A frog is crossing a river. The river is divided into x units and at each unit
there may or may not exist a stone. The frog can jump on a stone, but it must
not jump into the water.

Given a list A of size N giving stones' positions (in units) in sorted
ascending order, determine if the frog is able to cross the river by landing
on the last stone. Initially, the frog is on the first stone and assume the
first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1,
k, or k + 1 units. Note that the frog can only jump in the forward direction.
Input Format

The first and only argument given is the integer array A.
Output Format

Return 0 if it is not possible to land on last stone, else return 1
Constraints

2 <= N <= 1000
1 <= A[i] <= 1000000
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if A[1] - A[0] != 1:
            return 0
        n = len(A)
        k_vals_map = {pos: set() for pos in A}
        k_vals_map[A[1]].add(1)
        for i in range(n-1):
            pos = A[i]
            for k in k_vals_map[pos]:
                for new_k in (k-1, k, k+1):
                    if new_k > 0 and pos + new_k in k_vals_map:
                        k_vals_map[pos + new_k].add(new_k)
        if len(k_vals_map[A[-1]]) > 0:
            return 1
        return 0
