"""
Given any source point, (C, D) and destination point, (E, F) on a chess board
of size A x B, we need to find whether Knight can move to the destination or
not.

The above figure details the movements for a knight ( 8 possibilities ).
If yes, then what would be the minimum number of steps for the knight to move
to the said point. If knight can not move from the source point to the
destination point, then return -1.

NOTE: A knight cannot go out of the board.

Problem Constraints
1 <= A, B <= 500
"""

from collections import deque


# @param A : integer
# @param B : integer
# @param C : integer
# @param D : integer
# @param E : integer
# @param F : integer
# @return an integer
def knight(A, B, C, D, E, F):
    n, m = A, B
    c, d, e, f = C, D, E, F
    if c < 1 or c > n or d < 1 or d > m or e < 1 or e > n or f < 1 or f > m:
        return -1
    visited = [[False for _ in range(m)] for _ in range(n)]
    directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1),
                  (1, -2), (-1, -2)]

    queue = deque([(c, d, 0)])
    visited[c - 1][d - 1] = True

    while queue:
        x, y, steps = queue.popleft()
        if x == e and y == f:
            return steps
        for direction in directions:
            new_x, new_y = x + direction[0], y + direction[1]
            if 1 <= new_x <= n and 1 <= new_y <= m and not \
            visited[new_x - 1][new_y - 1]:
                queue.append((new_x, new_y, steps + 1))
                visited[new_x - 1][new_y - 1] = True

    return -1
