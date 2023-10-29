"""
Given an array A of N integers.
Find the largest continuous sequence in a array which sums to zero.

Problem Constraints
1 <= N <= 10^6
-10^7 <= A[i] <= 10^7

Solution explanation: we initialize the sum-index map with {0: -1} to cover cases where the sequence starts from the
first element and ends at index i
"""


# @param A : list of integers
# @return a list of integers
def lszero(A):
    n = len(A)
    prefix_sum = [A[0]] * n
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]

    si_map = {0: -1}
    left, right, max_len = -1, -1, 0
    for i in range(n):
        pref_sum = prefix_sum[i]
        if pref_sum in si_map:
            prev_index = si_map[pref_sum]
            if i - prev_index > max_len:
                left, right = prev_index, i
                max_len = i - prev_index
        else:
            si_map[pref_sum] = i

    return A[left + 1:right + 1]


arr = [1, 2, -3]
print(lszero(arr))
