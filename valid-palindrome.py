class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = ''.join([l if l.isalpha() or l.isdigit() else '' for l in s.lower()])
        for i in range(0, (len(s)+1)/2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True


t1 = Solution()
print t1.isPalindrome("A man, a plan, a canal: Panama")
print t1.isPalindrome("race a car")
print t1.isPalindrome('1a2')
