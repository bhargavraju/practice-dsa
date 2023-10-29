"""
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a
given integer B in array A.
Your algorithm's runtime complexity must be in the order of O(log n).
Return an array of size 2, such that first element = starting position of B in A and
second element = ending position of B in A, if B is not found in A return [-1, -1].
"""


# @param A : tuple of integers
# @param B : integer
# @return a list of integers
def searchRange(A, B):
    n = len(A)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == B:
            ll, lr, l_ans = 0, mid, mid
            while ll <= lr:
                l_mid = (ll + lr) // 2
                if A[l_mid] == B:
                    l_ans = l_mid
                    lr = l_mid - 1
                else:
                    ll = l_mid + 1
            rl, rr, r_ans = mid, n - 1, mid
            while rl <= rr:
                r_mid = (rl + rr) // 2
                if A[r_mid] == B:
                    r_ans = r_mid
                    rl = r_mid + 1
                else:
                    rr = r_mid - 1
            return [l_ans, r_ans]
        elif A[mid] < B:
            left = mid + 1
        else:
            right = mid - 1
    return [-1, -1]
