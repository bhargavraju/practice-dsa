"""
There is a rectangle with left bottom as (0, 0) and right up as (x, y).
There are N circles such that their centers are inside the rectangle.
Radius of each circle is R. Now we need to find out if it is possible that we
can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjacent neighbours and we
cannot move outside the boundary of the rectangle at any point of time.


Problem Constraints
0 <= x , y, R <= 100
1 <= N <= 1000
Center of each circle would lie within the grid


Input Format
1st argument given is an Integer x , denoted by A in input.
2nd argument given is an Integer y, denoted by B in input.
3rd argument given is an Integer N, number of circles, denoted by C in input.
4th argument given is an Integer R, radius of each circle, denoted by D in input.
5th argument given is an Array A of size N, denoted by E in input,
where A[i] = x cordinate of ith circle
6th argument given is an Array B of size N, denoted by F in input,
where B[i] = y cordinate of ith circle


Output Format
Return YES or NO depending on weather it is possible to reach cell (x,y) or
not starting from (0,0).
"""

from collections import deque


# @param A : integer
# @param B : integer
# @param C : integer
# @param D : integer
# @param E : list of integers
# @param F : list of integers
# @return a strings
def solve(A, B, C, D, E, F):
    n, m, N, R, A, B = A + 1, B + 1, C, D, E, F
    arr = [[1 for _ in range(m)] for _ in range(n)]
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1),
                  (0, -1), (-1, -1)]

    for i in range(n):
        for j in range(m):
            for k in range(N):
                if pow(i - A[k], 2) + pow(j - B[k], 2) <= R * R:
                    arr[i][j] = 0
                    break

    if arr[0][0] == 0 or arr[n - 1][m - 1] == 0:
        return 'NO'

    st = deque()
    st.append((0, 0))
    arr[0][0] = 0
    while st:
        x, y = st.pop()
        if x == n - 1 and y == m - 1:
            return 'YES'
        for direction in directions:
            new_x, new_y = x + direction[0], y + direction[1]
            if 0 <= new_x < n and 0 <= new_y < m and arr[new_x][
                new_y] == 1:
                st.append((new_x, new_y))
                arr[new_x][new_y] = 0

    return 'NO'
