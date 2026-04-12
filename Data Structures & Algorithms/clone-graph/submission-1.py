"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        cloned = {}

        def dfs(copy):
            if copy in cloned:
                return cloned[copy]

            new_node = Node(copy.val)
            cloned[copy] = new_node
            for nei in copy.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            return new_node

        return dfs(node)



        