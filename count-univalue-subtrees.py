# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]
        def uni(root):
            if root is None:
                return True
            flag = True
            if not uni(root.left):
                flag = False
            if not uni(root.right):
                flag = False
            if root.left is not None and root.val != root.left.val:
                flag = False
            if root.right is not None and root.val != root.right.val:
                flag = False
            if flag:
                ans[0] += 1
                return True
            return False
        uni(root)
        return ans[0]
