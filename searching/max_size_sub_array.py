"""
You have been given an array A having N elements and an integer S.
You have to find a maximum number X such that sum of all its sub arrays of size X is less than or equal to S.
You may assume that X will always exist.
"""


# @param A : list of integers
# @param B : integer
# @return an integer
def solve(A, B):
    n = len(A)
    prefix_sum = [A[0]] * n
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]

    def sum_is_less_than_b(x):
        l, r = 0, x - 1
        while r < n:
            sum_of_subarray = prefix_sum[r]
            if l - 1 >= 0:
                sum_of_subarray -= prefix_sum[l - 1]
            if sum_of_subarray > B:
                return False
            else:
                l += 1
                r += 1
        return True

    left, right, ans = 1, n, 1
    while left <= right:
        mid = (left + right) // 2
        if sum_is_less_than_b(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
