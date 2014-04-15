# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root is None:
            return 0
        maxPath, maxArm = self.calc(root);
        return maxPath

    def calc(self, root):
        leftMaxPath, leftMaxArm, rightMaxPath, rightMaxArm = None,None,None,None
        if root.left:
            leftMaxPath, leftMaxArm = self.calc(root.left)
        if root.right:
            rightMaxPath, rightMaxArm = self.calc(root.right)
        
        maxPath = max(root.val, leftMaxPath, rightMaxPath,
                leftMaxArm + root.val if leftMaxArm else None,
                rightMaxArm + root.val if rightMaxArm else None,
                leftMaxArm+root.val+rightMaxArm if leftMaxArm and rightMaxArm else None)
        maxArm = max(leftMaxArm + root.val if leftMaxArm else None,
                    rightMaxArm + root.val if rightMaxArm else None,
                    root.val)
        return maxPath, maxArm


tree1 = TreeNode(1, left = TreeNode(1),
                    right = TreeNode(6, left = TreeNode(8),
                                        right = TreeNode(10)))
tree2 = TreeNode(1, left = TreeNode(2),
                    right = TreeNode(3))
tree3 = TreeNode(-3)

s = Solution()
print s.maxPathSum(tree1)
print s.maxPathSum(tree2)
print s.maxPathSum(tree3)
