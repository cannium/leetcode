class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        for w in words:
            if len(w) != len(pattern):
                continue
            m = {}
            d = {}
            match = True
            for i in range(len(w)):
                a = pattern[i]
                b = w[i]
                if a in m:
                    if m[a] != b:
                        match = False
                        break
                else:
                    if b in d:
                        match = False
                        break
                    m[a] = b
                    d[b] = 1
            if match:
                ans.append(w)
        return ans
