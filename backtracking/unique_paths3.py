"""
Given a matrix of integers A of size N x M . There are 4 types of squares in it:

1. 1 represents the starting square.  There is exactly one starting square.
2. 2 represents the ending square.  There is exactly one ending square.
3. 0 represents empty squares we can walk over.
4. -1 represents obstacles that we cannot walk over.
Find and return the number of 4-directional walks from the starting square to the ending square, that walk over
every non-obstacle square exactly once.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.

Problem Constraints
2 <= N * M <= 20
-1 <= A[i] <= 2
"""


# @param A : list of list of integers
# @return an integer
def solve(A):
    n = len(A)
    m = len(A[0])
    start_i, start_j = -1, -1
    empty = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                empty += 1
            elif A[i][j] == 1:
                start_i, start_j = i, j

    ans = 0

    def rec_helper(arr, curr_i, curr_j, curr_empty_count):
        nonlocal ans
        if arr[curr_i][curr_j] == 2:
            if curr_empty_count == empty:
                ans += 1
            return
        if arr[curr_i][curr_j] == 0:
            curr_empty_count += 1
        arr[curr_i][curr_j] = -1
        if curr_i - 1 >= 0 and arr[curr_i - 1][curr_j] != -1:
            rec_helper(arr, curr_i - 1, curr_j, curr_empty_count)
        if curr_i + 1 < n and arr[curr_i + 1][curr_j] != -1:
            rec_helper(arr, curr_i + 1, curr_j, curr_empty_count)
        if curr_j - 1 >= 0 and arr[curr_i][curr_j - 1] != -1:
            rec_helper(arr, curr_i, curr_j - 1, curr_empty_count)
        if curr_j + 1 < m and arr[curr_i][curr_j + 1] != -1:
            rec_helper(arr, curr_i, curr_j + 1, curr_empty_count)
        arr[curr_i][curr_j] = 0

    rec_helper(A, start_i, start_j, 0)
    return ans


test = [
  [1, 0],
  [0, 0],
  [2, -1]
]
print(solve(test))
