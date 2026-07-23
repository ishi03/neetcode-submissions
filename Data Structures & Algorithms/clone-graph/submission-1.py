"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.clones = dict()
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        # we are passed a node
        # first copy the node
        # then copy the neighbours
        new = Node(node.val)
        neighbors = new.neighbors
        self.clones[node] = new
        for n in node.neighbors:
            if n in self.clones:
                neighbors.append(self.clones[n])
            else:
                # clone the neighbor first
                n_clone = self.cloneGraph(n)
                self.clones[n] = n_clone
                neighbors.append(n_clone)
        # new = Node(node.val, neighbors)
        return new
        