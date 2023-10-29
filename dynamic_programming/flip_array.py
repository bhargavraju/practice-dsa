"""
Given an array A of positive elements, you have to flip the sign of some of
its elements such that the resultant sum of the elements of array should be
minimum non-negative(as close to zero as possible).

Return the minimum number of elements whose sign needs to be flipped such
that the resultant sum is minimum non-negative.

Problem Constraints
1 <= length of(A) <= 100
Sum of all the elements will not exceed 10,000.
"""


# We have two sacks one negative, another positive. The negative sack has max
# capacity of half the total sum. The weight of each number can be considered
# it's 'value'. The loss/value of each number is '1' and this loss has to be
# minimized.


# @param A : tuple of integers
# @return an integer
def solve(A):
    n = len(A)
    total_sum = sum(A)
    capacity = total_sum//2
    dp = [[float('inf')]*(capacity+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if A[i-1] <= j:
                dp[i][j] = min(dp[i-1][j], 1 + dp[i-1][j-A[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    for j in range(capacity, -1, -1):
        if dp[n][j] != float('inf'):
            return dp[n][j]
