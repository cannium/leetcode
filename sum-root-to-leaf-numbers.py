# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root == None:
            return 0
        self.numbers = []
        self.travel(root)
        return sum(self.numbers)

    def travel(self, root):
        root.val = str(root.val)
        if root.left:
            root.left.val = root.val + str(root.left.val)
            self.travel(root.left)
        if root.right:
            root.right.val = root.val + str(root.right.val)
            self.travel(root.right)
        if root.left == None and root.right == None:
            self.numbers.append(int(root.val))
