# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def do(root):
    if root.left is None and root.right is None:
        return root, root
    new_root, attach = do(root.left)
    attach.left = root.right
    attach.right = root
    root.left, root.right = None, None
    return new_root, attach.right

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        new_root, _ = do(root)
        return new_root
