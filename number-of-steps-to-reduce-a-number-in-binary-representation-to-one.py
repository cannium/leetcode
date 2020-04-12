class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = int(s, 2)
        step = 0
        while n != 1:
            step += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = n + 1
        return step

s = Solution()
print s.numSteps('1101')
print s.numSteps('10')
print s.numSteps('1')

