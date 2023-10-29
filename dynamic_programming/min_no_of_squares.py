"""
Given an integer A. Return minimum count of numbers, sum of whose squares is
equal to A.


Problem Constraints
1 <= A <= 10^5
"""


# @param A : integer
# @return an integer
def countMinSquares(A):
    min_count = [float('inf')]*(A+1)
    min_count[0] = 0
    min_count[1] = 1
    for i in range(2, A+1):
        j = 1
        while j*j <= i:
            min_count[i] = min(min_count[i], 1 + min_count[i-j*j])
            j += 1
    return min_count[A]
