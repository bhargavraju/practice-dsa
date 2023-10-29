"""
Given a matrix of integers A of size N x M describing a maze. The maze
consists of empty locations and walls. 1 represents a wall in a matrix and 0
represents an empty location in a wall. There is a ball trapped in a maze.
The ball can go through empty spaces by rolling up, down, left or right,
but it won't stop rolling until hitting a wall (maze boundary is also
considered as a wall). When the ball stops, it could choose the next direction.

Given two array of integers of size B and C of size 2 denoting the starting
and destination position of the ball.

Find the shortest distance for the ball to stop at the destination. The
distance is defined by the number of empty spaces traveled by the ball from
the starting position (excluded) to the destination (included). If the ball
cannot stop at the destination, return -1.

Problem Constraints
2 <= N, M <= 100
0 <= A[i] <= 1
0 <= B[i][0], C[i][0] < N
0 <= B[i][1], C[i][1] < M

Input Format
The first argument given is the integer matrix A.
The second argument given is an array of integer B.
The third argument if an array of integer C.

Output Format
Return a single integer, the minimum distance required to reach destination
"""


from collections import deque


# @param A : list of list of integers
# @param B : list of integers
# @param C : list of integers
# @return an integer
def solve(A, B, C):
    n = len(A)
    m = len(A[0])
    start_x, start_y = B[0], B[1]
    end_x, end_y = C[0], C[1]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    distances = [[-1 for _ in range(m)] for _ in range(n)]
    queue = deque([(start_x, start_y, 0)])

    while queue and distances[end_x][end_y] == -1:
        x, y, d = queue.popleft()
        if distances[x][y] != -1:
            continue
        distances[x][y] = d
        for dr in directions:
            x_delta, y_delta = dr[0], dr[1]
            x1, y1, d1 = x + x_delta, y + y_delta, 1
            while 0 <= x1 < n and 0 <= y1 < m and A[x1][y1] == 0:
                x1, y1, d1 = x1 + x_delta, y1 + y_delta, d1 + 1
            x1, y1, d1 = x1 - x_delta, y1 - y_delta, d1 - 1
            if d1 > 0 and distances[x1][y1] == -1:
                queue.append((x1, y1, d + d1))

    return distances[end_x][end_y]
