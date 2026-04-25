"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        res = [] 
        visited = set() 
        hashmap = {} #oldNode: newNode 
        if not node:
            return node

        def create_hashmap(oldNode):
            if oldNode in hashmap or not oldNode:
                return 
            else:
                newNode = Node(oldNode.val)
                hashmap[oldNode] = newNode

                if oldNode.neighbors:
                    for neighbor in oldNode.neighbors:
                        create_hashmap(neighbor)
            return hashmap
        
        create_hashmap(node)
        for oldNode,newNode in hashmap.items():
            if oldNode.neighbors:
                for oldNeighbor in oldNode.neighbors: 
                    newNode.neighbors.append(hashmap[oldNeighbor])
        return hashmap[node]






