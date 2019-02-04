class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = {}
        for i in range(len(words)):
            w = words[i]
            if w in self.d:
                self.d[w].append(i)
            else:
                self.d[w] = [i]
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1  = self.d[word1]
        l2 = self.d[word2]
        ans = float('inf')
        for i in l1:
            for j in l2:
                if abs(i-j) < ans:
                    ans = abs(i-j)
        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
