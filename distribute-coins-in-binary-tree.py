# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node(object):
    def __init__(self, x):
        self.parent = None
        self.left = None
        self.right = None
        self.val = x
        self.leftreq = 0
        self.rightreq = 0
        
def build(originRoot, root):
    if originRoot.left is not None:
        root.left = Node(originRoot.left.val)
        build(originRoot.left, root.left)
    if originRoot.right is not None:
        root.right = Node(originRoot.right.val)
        build(originRoot.right, root.right)
        
def calc_req(root):
    if root is None:
        return 0
    root.leftreq = calc_req(root.left)
    root.rightreq = calc_req(root.right)
    return 1 + root.leftreq + root.rightreq - root.val

def calc(root):
    ans = 0
    if root.leftreq < 0:
        root.val -= root.leftreq
        ans -= root.leftreq
    if root.rightreq < 0:
        root.val -= root.rightreq
        ans -= root.rightreq
    if root.leftreq > 0:
        root.left.val += root.leftreq
        ans += root.leftreq
    if root.rightreq > 0:
        root.right.val += root.rightreq
        ans += root.rightreq
    if root.left is not None:
        ans += calc(root.left)
    if root.right is not None:
        ans += calc(root.right)
    return ans
        

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        r = Node(root.val)
        build(root, r)
        calc_req(r)
        return calc(r)
