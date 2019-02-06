# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def n2s(n):
    return chr(n+ord('a'))

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        q = [(root, '')]
        words = []
        while len(q) > 0:
            next_q = []
            for node, s in q:
                w = n2s(node.val) + s
                if node.left is None and node.right is None:
                    words.append(w)
                    continue
                if node.left:
                    next_q.append((node.left, w))
                if node.right:
                    next_q.append((node.right, w))
            q = next_q
        return sorted(words)[0]
        
