class Solution(object):
    def shortestDistance(self, words, word1, word2):
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
        l1 = d[word1]
        l2 = d[word2]
        ans = float('inf')
        for i in l1:
            last = None
            for j in l2:
                a = abs(i-j)
                if last and a > last:
                    break
                last = a
                if a < ans:
                    ans = a
        return ans
