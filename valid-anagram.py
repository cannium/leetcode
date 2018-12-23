class Solution(object):
    def memo(self, s):
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        return d
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d1 = self.memo(s)
        d2 = self.memo(t)
        for c in s:
            if c not in d2:
                return False
            if d1[c] != d2[c]:
                return False
        return True
