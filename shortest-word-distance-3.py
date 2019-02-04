class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = {}
        for i in range(len(words)):
            w = words[i]
            if w in d:
                d[w].append(i)
            else:
                d[w] = [i]
        ans = float('inf')
        if word1 == word2:
            l = d[word1]
            for i in range(1, len(l)):
                if abs(l[i]-l[i-1]) < ans:
                    ans = abs(l[i]-l[i-1])
            return ans
        l1 = d[word1]
        l2 = d[word2]
        for i in l1:
            for j in l2:
                if abs(i-j) < ans:
                    ans = abs(i-j)
        return ans
