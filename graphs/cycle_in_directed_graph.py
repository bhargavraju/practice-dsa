"""
Given an directed graph having A nodes. A matrix B of size M x 2 is given
which represents the M edges such that there is a edge directed from node
B[i][0] to node B[i][1].

Find whether the graph contains a cycle or not, return 1 if cycle is present
else return 0.

NOTE:
The cycle must contain at least two nodes.
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

Input Format
The first argument given is an integer A representing the number of nodes in
the graph.
The second argument given a matrix B of size M x 2 which represents the M
edges such that there is a edge directed from node B[i][0] to node B[i][1].

Output Format
Return 1 if cycle is present else return 0.
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(2000005)


def dfs(node, curr_traversal, visited, al):
    if node in curr_traversal:
        return True
    curr_traversal.add(node)
    visited[node-1] = True

    for neighbour in al[node]:
        if dfs(neighbour, curr_traversal, visited, al):
            return True
        curr_traversal.remove(neighbour)
    return False


# @param A : integer
# @param B : list of list of integers
# @return an integer
def solve(A, B):
    al = defaultdict(list)
    for edge in B:
        al[edge[0]].append(edge[1])
    visited = [False for _ in range(A)]
    for i in range(1, A+1):
        if visited[i-1]:
            continue
        if dfs(i, set(), visited, al):
            return 1
    return 0
