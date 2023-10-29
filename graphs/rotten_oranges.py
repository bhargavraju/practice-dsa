"""
Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

Each cell can have three values:
The value 0 representing an empty cell.
The value 1 representing a fresh orange.
The value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom)
to a rotten orange becomes rotten. Return the minimum number of minutes that
must elapse until no cell has a fresh orange.
If this is impossible, return -1 instead.


Problem Constraints
1 <= N, M <= 1000
0 <= A[i][j] <= 2
"""

from collections import deque


# @param A : list of list of integers
# @return an integer
def solve(A):
    n = len(A)
    m = len(A[0])
    queue = deque()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    time = 0

    for i in range(n):
        for j in range(m):
            if A[i][j] == 2:
                queue.append((i, j, 0))

    while queue:
        x, y, t = queue.popleft()
        time = max(time, t)
        for direction in directions:
            new_x, new_y = x + direction[0], y + direction[1]
            if 0 <= new_x < n and 0 <= new_y < m and A[new_x][new_y] == 1:
                A[new_x][new_y] = 2
                queue.append((new_x, new_y, t + 1))

    for i in range(n):
        for j in range(m):
            if A[i][j] == 1:
                return -1

    return time
