"""
Given a weighted undirected graph having A nodes and M weighted edges, and a
source node C.
You have to find an integer array D of size A such that:
=> D[i] : Shortest distance form the C node to node i.
=> If node i is not reachable from C then -1.

Note:
There are no self-loops in the graph.
No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are numbered from 0 to A-1.
Your solution will run on multiple testcases. If you are using global
variables make sure to clear them.

Problem Constraints
1 <= A <= 1e5
0 <= B[i][0],B[i][1] < A
0 <= B[i][2] <= 1e3
0 <= C < A

Input Format
The first argument given is an integer A, representing the number of nodes.
The second argument given is the matrix B of size M x 3, where nodes B[i][0]
and B[i][1] are connected with an edge of weight B[i][2].
The third argument given is an integer C.

Output Format
Return the integer array D.
"""
import heapq
from collections import defaultdict


def solve(A, B, C):
    distances = defaultdict(dict)
    for e in B:
        l, r, d = e[0], e[1], e[2]
        distances[l][r] = d
        distances[r][l] = d
    res = [-1 for _ in range(A)]
    heap = [(0, C)]
    while heap:
        distance, node = heapq.heappop(heap)
        if res[node] != -1:
            continue
        res[node] = distance
        for k, v in distances[node].items():
            if res[k] == -1:
                heapq.heappush(heap, (distance + v, k))
    return res
