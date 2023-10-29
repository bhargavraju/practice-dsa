"""
Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the
array represents the location of the stall, and an integer B which represent the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall.
To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that
the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

Problem Constraints
2 <= N <= 100000
0 <= A[i] <= 109
2 <= B <= N
"""


# @param A : list of integers
# @param B : integer
# @return an integer
def solve(A, B):
    A.sort()

    def is_possible(k):
        cows = 1
        last = A[0]
        for i in range(1, len(A)):
            gap = A[i] - last
            if gap >= k:
                cows += 1
                last = A[i]
                if cows == B:
                    return True
        return False

    min_gap = A[1] - A[0]
    for i in range(1, len(A)):
        min_gap = min(min_gap, A[i] - A[i - 1])
    left, right, ans = min_gap, A[-1] - A[0], min_gap
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
