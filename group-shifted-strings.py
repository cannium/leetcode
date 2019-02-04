def dist(c1, c2):
    return (ord(c2) + 26 - ord(c1)) % 26

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strings:
            pattern = []
            for i in range(1, len(s)):
                pattern.append(dist(s[i], s[i-1]))
            pattern = tuple(pattern)
            if pattern in d:
                d[pattern].append(s)
            else:
                d[pattern] = [s]
        ans = []
        for k in d:
            ans.append(d[k])
        return ans
            
