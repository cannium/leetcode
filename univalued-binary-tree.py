# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isUni(root, v):
    if root is None:
        return True
    if root.val != v:
        return False
    return isUni(root.left, v) and isUni(root.right, v)

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        v = root.val
        return isUni(root.left, v) and isUni(root.right,  v)
        