"""
Misha loves eating candies. She has given N boxes of Candies.

She decides, every time she will choose a box having the minimum number of
candies, eat half of the candies and put the remaining candies in the
other box that has the minimum number of candies. Misha does not like a box if
it has the number of candies greater than B so she won't eat from that box.
Can you find how many candies she will eat?

NOTE 1: If a box has an odd number of candies then Misha will eat floor(odd/2).
NOTE 2: A same box will not be chosen again.
"""

import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        heapq.heapify(A)

        total_candies = 0
        while A[0] <= B:
            min_candies = heapq.heappop(A)
            total_candies += min_candies // 2
            candies_to_be_added = min_candies - (min_candies // 2)
            if A:
                new_min_candies = A[0]
                heapq.heapreplace(A, new_min_candies + candies_to_be_added)
            else:
                break

        return total_candies
