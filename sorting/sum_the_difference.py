"""
Given an integer array A of size N.
You have to find all possible non-empty subsequence of the array of numbers and then, for each subsequence,
find the difference between the largest and smallest numbers in that subsequence
Then add up all the differences to get the number.

As the number may be large, output the number modulo 1e9 + 7 (1000000007).

NOTE: Subsequence can be non-contiguous.

Problem Constraints
1 <= N <= 10000
1<= A[i] <=1000

Explanation at:
https://www.geeksforgeeks.org/find-sum-maximum-difference-possible-subset-given-array/
"""


def solve(A):
    min_sum, max_sum = 0, 0
    A.sort()
    n = len(A)
    for i in range(n):
        min_sum = 2 * min_sum + A[i]
        min_sum %= 1000000007
        max_sum = 2 * max_sum + A[n - 1 - i]
        max_sum %= 1000000007
    return (max_sum - min_sum + 1000000007) % 1000000007
