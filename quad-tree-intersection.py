"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1 is None:
            return quadTree2
        if quadTree2 is None:
            return quadTree1
        root = Node(None, False, None, None, None, None)
        if (quadTree1.isLeaf and quadTree1.val) or (quadTree2.isLeaf and quadTree2.val):
            root.val = True
            root.isLeaf = True
            return root
        if quadTree1.isLeaf:
            return quadTree2
        if quadTree2.isLeaf:
            return quadTree1
        root.topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        root.topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        root.bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        root.bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        if root.topLeft.val and root.topLeft.val == root.topRight.val == root.bottomLeft.val == root.bottomRight.val:
            root.val = root.topLeft.val
            root.isLeaf = True
            root.topLeft, root.topRight, root.bottomLeft, root.bottomRight = None, None, None, None
        return root
