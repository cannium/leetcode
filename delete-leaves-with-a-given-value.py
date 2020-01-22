# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def d(root, target):
    if root is None:
        return True
    leftDelete = d(root.left, target)
    if leftDelete:
        root.left = None
    rightDelete = d(root.right, target)
    if rightDelete:
        root.right = None
    if leftDelete and rightDelete and root.val == target:
        return True
    return False

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if d(root, target):
            return None
        else:
            return root