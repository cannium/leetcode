class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lens = len(s)
        lent = len(t)
        if abs(lens-lent) >= 2:
            return False
        change = 0
        if lens == lent:
            for i in range(lent):
                if s[i] != t[i]:
                    change += 1
                    if change > 1:
                        return False
            if change == 0:
                return False
            return True
        if lens < lent:
            s,t = t,s
            lens, lent = lent, lens
        j = 0
        i = 0
        while i < lent:
            if t[i] != s[j]:
                j += 1
                change += 1
                if change > 1:
                    return False
                continue
            i += 1
            j += 1
        return True
