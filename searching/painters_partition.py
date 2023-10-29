"""
Given 2 integers A and B and an array of integers C of size N. Element C[i] represents length of ith board.
You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes
B units of time to paint 1 unit of board.

Calculate and return minimum time required to paint all boards under the constraints that any painter will
only paint contiguous sections of board.
NOTE:
1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter,
and partially by another.
2. A painter will only paint contiguous boards. Which means a configuration where painter 1 paints board 1 and 3
but not 2 is invalid.

Return the ans % 10000003.

Problem Constraints
1 <= A <= 1000
1 <= B <= 106
1 <= N <= 105
1 <= C[i] <= 106
"""


# @param A : integer
# @param B : integer
# @param C : list of integers
# @return an integer
def paint(A, B, C):
    def is_possible(k):
        painters = 1
        units_of_board = 0
        for i in range(len(C)):
            if C[i] > k:
                return False
            if units_of_board + C[i] > k:
                units_of_board = C[i]
                painters += 1
                if painters > A:
                    return False
            else:
                units_of_board += C[i]
        return True

    left, right, ans = max(C), sum(C), sum(C)
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return (ans % 10000003 * B % 10000003) % 10000003
