# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.old2New = {}

    def cloneGraph(self, node):
        if node == None:
            return None
        l = [node]
        newNodes = []
        while l:
            n = l.pop(0)
            if self.old2New.get(n, None) == None:
                self.old2New[n] = UndirectedGraphNode(n.label)
            newNode = self.old2New[n]
            newNodes.append(newNode)
            for neighbor in n.neighbors:
                if self.old2New.get(neighbor, None) == None:
                    self.old2New[neighbor] = UndirectedGraphNode(neighbor.label)
                    l.append(neighbor)
                newNode.neighbors.append(self.old2New[neighbor])
        return newNodes[0]
