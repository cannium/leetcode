# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
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
