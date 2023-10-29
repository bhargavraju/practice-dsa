"""
Given an integer array A of size N. Find the contiguous sub array within the
given array (containing at least one number) which has the largest product.
Return an integer corresponding to the maximum product possible.

NOTE: Answer will fit in 32-bit integer value.


Problem Constraints
1 <= N <= 5 * 10^5
-100 <= A[i] <= 100
"""

# Kadence algorithm


# @param A : tuple of integers
# @return an integer
def maxProduct(A):
    n = len(A)
    max_arr = [0]*n
    min_arr = [0]*n
    max_arr[0] = A[0]  # max_product of a sub array 'ending' with A[i]
    min_arr[0] = A[0]  # min_product of a sub array 'ending' with A[i]
    for i in range(1, n):
        max_arr[i] = max(A[i], A[i]*max_arr[i-1], A[i]*min_arr[i-1])
        min_arr[i] = min(A[i], A[i]*max_arr[i-1], A[i]*min_arr[i-1])
    return max(max_arr)
