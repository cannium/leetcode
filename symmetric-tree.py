# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sym(self, l):
        if len(l) <= 1:
            return True
        for i in range(len(l)/2):
            j = len(l) - 1 -i
            if l[i] and l[j]:
                if l[i].val != l[j].val:
                    return False
            if l[i] and (l[j] is None):
                return False
            if (l[i] is None) and l[j]:
                return False
        return True
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        now = [root]
        next = []
        while len(now) > 0:
            if not self.sym(now):
                return False
            for x in now:
                if x:
                    next += [x.left, x.right]
            now = next
            next = []
        return True
