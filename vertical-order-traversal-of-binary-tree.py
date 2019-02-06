# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def cmp(x, y):
    return x[0].val - y[0].val

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        d = {} # X coordinate -> []Node
        q = [(root,0)]
        while len(q) > 0:
            next_q = []
            for node, x in q:
                if x in d:
                    d[x].append(node.val)
                else:
                    d[x] = [node.val]
                if node.left:
                    next_q.append((node.left, x-1))
                if node.right:
                    next_q.append((node.right, x+1))
            q = sorted(next_q, cmp=cmp)
        ans = []
        for x in sorted(d.keys()):
            ans.append(d[x])
        return ans
        
