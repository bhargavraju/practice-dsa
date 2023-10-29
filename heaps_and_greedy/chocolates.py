"""
Given N bags, each bag contains Bi chocolates. There is a kid and a magician.
In one unit of time, kid chooses a random bag i, eats Bi chocolates, then
the magician fills the ith bag with floor(Bi/2) chocolates.

Find the maximum number of chocolates that kid can eat in A units of time.

NOTE:
floor() function returns the largest integer less than or equal to
a given number. Return your answer modulo 10^9+7

Problem Constraints
1 <= N <= 100000
0 <= B[i] <= INTMAX
0 <= A <= 10^5
"""


import heapq


# @param A : integer
# @param B : list of integers
# @return an integer
def nchoc(A, B):
    arr = list(map(lambda x: -x, B))
    heapq.heapify(arr)
    max_choc = 0
    for i in range(A):
        max_size = -arr[0]
        max_choc += max_size
        heapq.heapreplace(arr, -(max_size//2))
    return max_choc % 1000000007
