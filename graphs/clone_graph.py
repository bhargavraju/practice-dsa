"""
Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.


Problem Constraints
1 <= Number of nodes <= 10^5


Input Format
First and only argument is a node A denoting the root of the undirected graph.


Output Format
Return the node denoting the root of the new clone graph.
"""

# Definition for an undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


from collections import deque


# @param node, an undirected graph node
# @return an undirected graph node
def cloneGraph(node):
    queue = deque([node])
    mapping = {}
    mapping[node] = UndirectedGraphNode(node.label)

    while queue:
        curr_node = queue.popleft()

        for neighbor in curr_node.neighbors:
            if neighbor not in mapping:
                mapping[neighbor] = UndirectedGraphNode(neighbor.label)
                queue.append(neighbor)
            mapping[curr_node].neighbors.append(mapping[neighbor])

    return mapping[node]
