"""
Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions
surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in
that surrounded region.

Problem Constraints
1 <= N, M <= 1000

Input Format
First and only argument is a N x M character matrix A.

Output Format
Make changes to the input only as matrix is passed by reference.


Example Input
Input 1:
 A = [
       [X, X, X, X],
       [X, O, O, X],
       [X, X, O, X],
       [X, O, X, X]
     ]
Input 2:
 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]

Example Output
Output 1:
 After running your function, the board should be:
 A = [
       [X, X, X, X],
       [X, X, X, X],
       [X, X, X, X],
       [X, O, X, X]
     ]
Output 2:
 After running your function, the board should be:
 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]
"""

from collections import deque


# @param A : list of list of chars
def solve(A):
    n = len(A)
    m = len(A[0])
    arr = [['O'] * (m + 2)]
    for row in A:
        new_row = ['O'] + row + ['O']
        arr.append(new_row)
    arr.append(['O'] * (m + 2))

    visited = [[False for _ in range(m + 2)] for _ in range(n + 2)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    st = deque([(0, 0)])
    visited[0][0] = True

    while st:
        i, j = st.pop()

        for direction in directions:
            new_i, new_j = i + direction[0], j + direction[1]
            if 0 <= new_i < n + 2 and 0 <= new_j < m + 2 and arr[new_i][
                new_j] == 'O' and not visited[new_i][new_j]:
                st.append((new_i, new_j))
                visited[new_i][new_j] = True

    for i in range(n):
        for j in range(m):
            if A[i][j] == 'O' and not visited[i + 1][j + 1]:
                A[i][j] = 'X'
