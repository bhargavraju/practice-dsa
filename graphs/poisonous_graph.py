"""
You are given an undirected unweighted graph consisting of A vertices and M
edges given in a form of 2D Matrix B of size M x 2 where (B[i][0], B][i][1])
denotes two nodes connected by an edge.

You have to write a number on each vertex of the graph. Each number should be
1, 2 or 3. The graph becomes Poisonous if for each edge the sum of numbers on
vertices connected by this edge is odd.

Calculate the number of possible ways to write numbers 1, 2 or 3 on vertices
so the graph becomes poisonous. Since this number may be large, return it
modulo 998244353.

NOTE:
Note that you have to write exactly one number on each vertex.
The graph does not have any self-loops or multiple edges.
Nodes are labelled from 1 to A.

Problem Constraints
1 <= A <= 3*105
0 <= M <= 3*105
1 <= B[i][0], B[i][1] <= A
B[i][0] != B[i][1]


Input Format
First argument is an integer A denoting the number of nodes.
Second argument is an 2D Matrix B of size M x 2 denoting the M edges.


Output Format
Return one integer denoting the number of possible ways to write numbers 1,
 2 or 3 on the vertices of given graph so it becomes Poisonous . Since answer
 may be large, print it modulo 998244353.
"""


from collections import defaultdict, deque


# @param A : integer
# @param B : list of list of integers
# @return an integer
def solve(A, B):
    mapping = defaultdict(list)
    for edge in B:
        mapping[edge[0]].append(edge[1])
        mapping[edge[1]].append(edge[0])
    visited = [False for _ in range(A)]
    labels = ['' for _ in range(A)]

    def bfs(i):
        queue = deque([i])
        visited[i-1] = True
        labels[i-1] = 'C1'
        c1_count, c2_count = 1, 0

        while queue:
            node = queue.popleft()
            label = labels[node-1]

            for neighbor in mapping[node]:
                if labels[neighbor-1] == label:
                    return False, 0, 0
                if not visited[neighbor-1]:
                    visited[neighbor-1] = True
                    if label == 'C2':
                        labels[neighbor-1] = 'C1'
                        c1_count += 1
                    else:
                        labels[neighbor-1] = 'C2'
                        c2_count += 1
                    queue.append(neighbor)

        return True, c1_count, c2_count

    count = 1
    for i in range(1, A+1):
        if not visited[i-1]:
            possible, c1_count, c2_count = bfs(i)
            if not possible:
                return 0
            curr_count = 2**c1_count + 2**c2_count
            count = count * curr_count

    return count % 998244353
