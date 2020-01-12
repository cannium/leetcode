# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def dp(memo, i, j):
    if i < 1 or j < 1:
        return [None]
    if i > j:
        return [None]
    if i == j:
        return [TreeNode(i)]
    if (i, j) in memo:
        return memo[(i, j)]
    ans = []
    for x in range(i, j+1):
        l = dp(memo, i, x-1)
        r = dp(memo, x+1, j)
        for leftNode in l:
            for rightNode in r:
                root = TreeNode(x)
                root.left = leftNode
                root.right = rightNode
                ans.append(root)
    memo[(i,j)] = ans
    return ans

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        memo = {}
        return dp(memo, 1, n)