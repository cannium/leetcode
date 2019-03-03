def inter(d, s):
    if d is None:
        return s
    ans = {}
    for k in d:
        if k in s:
            ans[k] = min(d[k], s[k])
    return ans

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        d = None
        for w in A:
            s = {}
            for c in w:
                if c in s:
                    s[c] += 1
                else:
                    s[c] = 1
            d = inter(d, s)
        if d is None:
            return []
        ans = []
        for k in d:
            ans += [k] * d[k]
        return ans
        
