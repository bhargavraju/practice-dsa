"""
Given a weighted undirected graph having A nodes, a source node C and
destination node D. Find the shortest distance from C to D and if it is
impossible to reach node D from C then return -1.

You are expected to do it in Time Complexity of O(A + M).

Note:
There are no self-loops in the graph.
No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are Numbered from 0 to A-1.
Your solution will run on multiple testcases. If you are using global
variables make sure to clear them.

Problem Constraints
1 <= A <= 10^5
0 <= B[i][0], B[i][1] < A
1 <= B[i][2] <= 2
0 <= C < A
0 <= D < A

Input Format
The first argument given is an integer A, representing the number of nodes.
The second argument given is the matrix B, where B[i][0] and B[i][1] are
connected through an edge of weight B[i][2].
The third argument given is an integer C, representing the source node.
The fourth argument is an integer D, representing the destination node.

Note: B[i][2] will be either 1 or 2.

Output Format
Return the shortest distance from C to D. If it is impossible to reach node
D from C then return -1.
"""


# @param A : integer
# @param B : list of list of integers
# @param C : integer
# @param D : integer
# @return an integer
from collections import defaultdict, deque


def solve(A, B, C, D):
    al = defaultdict(list)
    visited = {i: False for i in range(A)}

    for e in B:
        l, r, d = e[0], e[1], e[2]
        if d == 2:
            temp_node = str(l) + str(r)
            al[l].append(temp_node)
            al[r].append(temp_node)
            al[temp_node] = [l, r]
            visited[temp_node] = False
        else:
            al[l].append(r)
            al[r].append(l)

    queue = deque([(C, 0)])
    visited[C] = True
    while queue:
        node, distance = queue.popleft()
        if node == D:
            return distance
        for adj_node in al[node]:
            if not visited[adj_node]:
                queue.append((adj_node, distance + 1))
                visited[adj_node] = True

    return -1
