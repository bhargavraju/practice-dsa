"""
Given a directed graph having A nodes labelled from 1 to A containing M edges
given by matrix B of size M x 2such that there is a edge directed from node
B[i][0] to node B[i][1].

Find whether a path exists from node 1 to node A.
Return 1 if path exists else return 0.

NOTE:
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global
variables make sure to clear them.

Problem Constraints
2 <= A <= 10^5
1 <= M <= min(200000,A*(A-1))
1 <= B[i][0], B[i][1] <= A
"""

from collections import deque


# @param A : integer
# @param B : list of list of integers
# @return an integer
def solve(A, B):
    adj_list = {}

    for edge in B:
        l, r = edge[0], edge[1]
        if l in adj_list:
            adj_list[l].append(r)
        else:
            adj_list[l] = [r]

    st = deque([1])
    visited = [False] * A

    while st:
        node = st.pop()
        visited[node - 1] = True

        if node == A:
            return 1

        if node in adj_list:
            for neighbour in adj_list[node]:
                if not visited[neighbour - 1]:
                    st.append(neighbour)

    return 0
