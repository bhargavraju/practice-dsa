"""
Given a undirected graph having A nodes. A matrix B of size M x 2 is given
which represents the edges such that there is an edge between
B[i][0] and B[i][1].

Find whether the given graph is bipartite or not.

A graph is bipartite if we can split it's set of nodes into two independent
subsets A and B such that every edge in the graph has one node in A and
another node in B

Note:
There are no self-loops in the graph.
No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are Numbered from 0 to A-1.
Your solution will run on multiple testcases.
If you are using global variables make sure to clear them.


Problem Constraints
1 <= A <= 100000
1 <= M <= min(A*(A-1)/2,200000)
0 <= B[i][0],B[i][1] < A


Input Format
The first argument given is an integer A.
The second argument given is the matrix B.


Output Format
Return 1 if the given graph is bipartite else return 0.
"""

from collections import defaultdict, deque


# @param A : integer
# @param B : list of list of integers
# @return an integer
def solve(A, B):
    arr = [0] * A
    al = defaultdict(list)

    for edge in B:
        al[edge[0]].append(edge[1])
        al[edge[1]].append(edge[0])

    def bfs(node):
        arr[node] = 1
        queue = deque([node])
        while queue:
            n = queue.popleft()
            for neighbour in al[n]:
                if arr[neighbour] == arr[n]:
                    return False
                if arr[neighbour] == 0:
                    arr[neighbour] = 1 if arr[n] == 2 else 2
                    queue.append(neighbour)
        return True

    for i in range(A):
        if arr[i] == 0:
            if not bfs(i):
                return 0

    return 1

