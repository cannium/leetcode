# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def xyin(x, y, q):
    count = 0
    for n in q:
        if n.val == x or n.val == y:
            count += 1
    return count

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        q = [root]
        while len(q) > 0:
            count = xyin(x,y,q)
            if count == 2:
                return True
            if count == 1:
                return False
            next_q = []
            for n in q:
                if n.left and n.right:
                    if n.left.val == x and n.right.val == y:
                        return False
                    if n.left.val == y and n.right.val == x:
                        return False
                if n.left:
                    next_q.append(n.left)
                if n.right:
                    next_q.append(n.right)
            q = next_q
        return False
