class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.split()
        s.reverse()
        if s == None:
            return ''
        return ' '.join(s)
