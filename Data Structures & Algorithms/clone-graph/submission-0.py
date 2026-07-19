"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}

        def dfs(node):
            if node in seen:
                return seen[node] #the copy

            copy = Node(node.val) #copy node
            seen[node] = copy #og node = copy node
            for neighbor in node.neighbors: #loop through neighbors
                copy.neighbors.append(dfs(neighbor))
            return copy

        if not node:
            return None
        else:
            return dfs(node)     