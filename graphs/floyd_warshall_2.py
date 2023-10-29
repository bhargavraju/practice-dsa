"""
Sheldon lives in a country with A cities (numbered from 1 to A) and B
bidirectional roads. Roads are denoted by integer array D, E and F of size M,
where D[i] and E[i] denotes the cities and F[i] denotes the distance between
the cities.

Now he has many lectures to give in the city and is running short of time, so
he asked you C queries, for each query i, find the shortest distance between
city G[i] and H[i].

If the two cities are not connected then the distance between them is assumed
to be -1.

Problem Constraints
1 <= A <= 200
1 <= B <= 200000
1 <= C <= 100000
1 <= F[i] <= 1000000
1 <= D[i], E[i], G[i], H[i] <= A
"""


# @param A : integer
# @param B : integer
# @param C : integer
# @param D : list of integers
# @param E : list of integers
# @param F : list of integers
# @param G : list of integers
# @param H : list of integers
# @return a list of integers
def solve(A, B, C, D, E, F, G, H):
    INF = float('inf')
    distances = [[INF for _ in range(A)] for _ in range(A)]
    for i in range(A):
        distances[i][i] = 0
    for i in range(len(D)):
        distances[D[i]-1][E[i]-1] = min(F[i], distances[D[i]-1][E[i]-1])
        distances[E[i]-1][D[i]-1] = min(F[i], distances[E[i]-1][D[i]-1])
    for k in range(A):
        for i in range(A):
            for j in range(A):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    ans = []
    for i in range(C):
        d = distances[G[i]-1][H[i]-1]
        ans.append(-1 if d == INF else d)
    return ans
