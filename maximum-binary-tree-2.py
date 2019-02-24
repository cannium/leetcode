# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def expand(root):
    if root is None:
        return []
    else:
        return merge(root.left, [root.val], root.right)

def merge(left, vals, right):
    return expand(left) + vals + expand(right)
        
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        A = expand(root)
        A.append(val)
        return self.constructMaximumBinaryTree(A)
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        maxn = 0
        maxi = -1
        for i in range(len(nums)):
            if nums[i] > maxn:
                maxi = i
                maxn = nums[i]
        root = TreeNode(maxn)
        #print nums, nums[:maxi], maxn, nums[maxi+1:]
        root.left = self.constructMaximumBinaryTree(nums[:maxi])
        root.right = self.constructMaximumBinaryTree(nums[maxi+1:])
        return root
