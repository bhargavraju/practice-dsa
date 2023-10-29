"""
Given character matrix A of O's and X's, where O = white, X = black.
Return the number of black shapes. A black shape consists of one or more
adjacent X's (diagonals not included)


Problem Constraints
1 <= |A|,|A[0]| <= 1000
A[i][j] = 'X' or 'O'


Input Format
The First and only argument is character matrix A.


Output Format
Return a single integer denoting number of black shapes.
"""

from collections import deque


# @param A : list of strings
# @return an integer
def black(A):
    n = len(A)
    m = len(A[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs(i, j):
        st = deque([(i, j)])
        visited[i][j] = True

        while st:
            x, y = st.pop()

            for direction in directions:
                new_x, new_y = x + direction[0], y + direction[1]
                if 0 <= new_x < n and 0 <= new_y < m and A[new_x][
                    new_y] == 'X' and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    st.append((new_x, new_y))

    count = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] == 'X' and not visited[i][j]:
                dfs(i, j)
                count += 1
    return count
