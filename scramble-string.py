def dp(memo, s1, s2):
    if s1 == s2:
        return True
    if len(s1) == 1 and len(s2) == 1:
        return False
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    if (s2, s1) in memo:
        return memo[(s2, s1)]
    ans = False
    for i in range(1, len(s1)):
        if dp(memo, s1[i:], s2[i:]) and \
            dp(memo, s1[:i], s2[:i]):
            ans = True
            break
        if dp(memo, s1[i:], s2[:len(s1)-i]) and \
            dp(memo, s1[:i], s2[len(s1)-i:]):
            ans = True
            break
    memo[(s1, s2)] = ans
    return ans

    
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        return dp(memo, s1, s2)


s = Solution()
print(s.isScramble('great', 'rgeat'))
print(s.isScramble('abcde', 'caebd'))