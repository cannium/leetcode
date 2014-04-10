class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def __init__(self):
        self.bookkeeping = {}

    def wordBreak(self, s, dict):
        if s == '':
            return True
        if(self.bookkeeping.get(s, None) != None):
            return self.bookkeeping[s]

        for word in dict:
            if s.startswith(word):
                new = s.replace(word, '')
                if(self.wordBreak(new, dict)):
                    self.bookkeeping[new] = True
                    return True
                else:
                    self.bookkeeping[new] = False
        return False


so = Solution()
#s = 'leetcodecode'
#d = ['leet', 'code', 'et']
#s = 'catsanddog'
#d = ["cat", "cats", "and", "sand", "dog"]
s = 'cars'
d = ["car","ca", "rs"]
print so.wordBreak(s, d)
