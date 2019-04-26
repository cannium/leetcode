# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def f(ancesters, root):
    if root is None:
        return 0
    ans = 0
    for a in ancesters:
        ans = max(ans, abs(a-root.val))
    new = ancesters[:]
    new.append(root.val)
    ans = max(ans, f(new, root.left), f(new, root.right))
    return ans

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return f([], root)
