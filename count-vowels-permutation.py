class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        sa, se, si, so, su = 1,1,1,1,1
        while n > 1:
            sa, se, si, so, su = se, sa+si, sa+se+so+su, si+su, sa
            n -= 1
        return sum([sa, se, si, so, su]) % (10**9 + 7)


s = Solution()
print s.countVowelPermutation(1)
print s.countVowelPermutation(2)
print s.countVowelPermutation(5)
print s.countVowelPermutation(20000)