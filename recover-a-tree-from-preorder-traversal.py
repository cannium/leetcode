# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def first(s):
    i = 0
    while i < len(s) and s[i] == '-':
        i += 1
        continue
    start = i
    while i < len(s) and s[i] != '-':
        i += 1
        continue
    return int(s[start:i]), i

def nexts(s, level):
    #print s, level
    start = None
    ans = []
    for i in range(len(s)):
        #print start, i, s[i]
        if s[i] != '-':
            if start is None:
                continue
            if i - start == level:
                ans.append(start)
            start = None
        else:
            if start is None:
                start = i
    return ans

def build(s, level):
    if len(s) == 0:
        return None
    val, i = first(s)
    root = TreeNode(val)
    s = s[i:]
    nextlevel = nexts(s, level + 1)
    if len(nextlevel) == 0:
        return root
    if len(nextlevel) == 1:
        #print s[nextlevel[0]:]
        root.left = build(s[nextlevel[0]:], level+1)
    else:
        #print s[nextlevel[0]:nextlevel[1]], s[nextlevel[1]:]
        root.left = build(s[nextlevel[0]:nextlevel[1]], level+1)
        root.right = build(s[nextlevel[1]:], level+1)
    return root
    
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        root = build(S, 0)
        return root
        
