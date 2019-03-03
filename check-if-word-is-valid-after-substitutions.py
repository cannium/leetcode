class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        if len(S) < 3:
            return False
        s = S
        while True:
            if len(s) == 0:
                return True
            i = s.find('abc')
            if i == -1:
                return False
            s = s[:i] + s[i+3:]
        
