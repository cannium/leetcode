# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        location = {}
        for i in xrange(len(voyage)):
            location[voyage[i]] = i
        if root != None and len(voyage) == 0:
            return [-1]
        if root == None and len(voyage) > 0:
            return [-1]
        if root == None and len(voyage) == 0:
            return []
        if root.val != voyage[0]:
            return [-1]
        ans = []
        if root.left is None and root.right is None:
            if len(voyage) > 1:
                return [-1]
            else:
                return ans
        if root.left is None:
            root.left, root.right = root.right, root.left
        lroot = root.left.val
        rroot = None
        if root.right is not None:
            rroot = root.right.val
        if len(voyage) <= 1:
            return [-1]
        if lroot != voyage[1] and rroot != voyage[1]:
            return [-1]
        if rroot == voyage[1]:
            ans.append(root.val)
            root.left, root.right = root.right, root.left
        lans = []
        rans = []
        if root.right is None:
            lans = self.flipMatchVoyage(root.left, voyage[1:])
        else:
            if root.right.val not in location:
                return [-1]
            lans = self.flipMatchVoyage(root.left, voyage[1:location[root.right.val]])
            rans = self.flipMatchVoyage(root.right, voyage[location[root.right.val]:])
        if -1 in lans or -1 in rans:
            return [-1]
        return ans + lans + rans
        
        
