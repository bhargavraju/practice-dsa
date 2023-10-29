"""
Find the largest distance Given an arbitrary unweighted rooted tree which
consists of N (2 <= N <= 40000) nodes.

The goal of the problem is to find the largest distance between two nodes in a
tree.
Distance between two nodes is a number of edges on a path between the nodes
(there will be a unique path between any pair of nodes since it is a tree).

The nodes will be numbered 0 through N - 1.
The tree is given as an array A, there is an edge between nodes
A[i] and i (0 <= i < N).
Exactly one of the i's will have A[i] equal to -1, it will be root node.

Problem Constraints
2 <= |A| <= 40000

Input Format
First and only argument is vector A

Output Format
Return the length of the longest path

Example Input
Input 1:
A = [-1, 0]
Input 2:
A = [-1, 0, 0]

Example Output
Output 1:
 1
Output 2:
 2
"""
from collections import deque, defaultdict


def get_farthest(n, root, edges):
    visited = [False for _ in range(n)]
    distances = [0 for _ in range(n)]
    queue = deque([(root, 0)])
    visited[root] = True
    while queue:
        node, d = queue.popleft()
        distances[node] = d

        for neighbour in edges[node]:
            if not visited[neighbour]:
                queue.append((neighbour, d + 1))
                visited[neighbour] = True

    farthest, distance = root, 0
    for i in range(n):
        if distances[i] > distance:
            farthest, distance = i, distances[i]
    return farthest, distance


# @param A : list of integers
# @return an integer
def solve(A):
    n = len(A)

    root = 0
    edges = defaultdict(list)
    for i in range(n):
        if A[i] == -1:
            root = i
            continue
        edges[i].append(A[i])
        edges[A[i]].append(i)

    farthest, _ = get_farthest(n, root, edges)
    _, ans = get_farthest(n, farthest, edges)

    return ans
