# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root is None:
            return ans
        stack = [root]
        while stack:
            n = stack.pop()
            if n.left is None and n.right is None:
                ans.append(n.val)
                continue
            node = TreeNode(n.val)
            stack.append(node)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
        return ans
