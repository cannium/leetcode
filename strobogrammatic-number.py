def rev(s):
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        processed = []
        for c in num:
            if c not in '01689':
                return False
            if c == '6':
                processed.append('9')
            elif c == '9':
                processed.append('6')
            else:
                processed.append(c)
        rev(processed)
        if ''.join(processed) == num:
            return True
        return False
