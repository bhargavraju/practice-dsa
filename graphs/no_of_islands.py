"""
Given a matrix of integers A of size N x M consisting of 0 and 1. A group of
connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you
can visit any cell that shares a corner with (i, j) and value in that cell is
1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:

(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.

Return the number of islands.

NOTE: Rows are numbered from top to bottom and columns are numbered
from left to right.


Problem Constraints
1 <= N, M <= 100
0 <= A[i] <= 1
"""

from collections import deque


# @param A : list of list of integers
# @return an integer
def solve(self, A):
    n = len(A)
    m = len(A[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    def bfs(i, j):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1),
                      (-1, 1), (1, -1)]
        queue = deque([(i, j)])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            for direction in directions:
                new_x, new_y = x + direction[0], y + direction[1]
                if 0 <= new_x < n and 0 <= new_y < m and A[new_x][new_y] == 1 and not visited[new_x][new_y]:
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = True

    count = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1

    return count
