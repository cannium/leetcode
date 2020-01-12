def allStar(j, p):
    for jj in range(j, len(p)):
        if p[jj] != '*':
            return False
    return True

def dp(memo, i, j, s, p):
    if i == len(s) and j == len(p):
        return True
    if j == len(p):
        return False
    if i == len(s):
        if allStar(j, p):
            return True
        else:
            return False
    if (i, j) in memo:
        return memo[(i,j)]
    if s[i] == p[j] or p[j] == '?':
        ans = dp(memo, i+1, j+1, s, p)
        memo[(i,j)] = ans
        return ans
    if p[j] == '*':
        ans = dp(memo, i+1, j, s, p) or \
            dp(memo, i, j+1, s, p) or \
            dp(memo, i+1, j+1, s, p)
        memo[(i,j)] = ans
        return ans
    return False
    

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return dp(memo, 0, 0, s, p)


s = Solution()
print( s.isMatch('aa', 'a'))
print( s.isMatch('aa', '*'))
print( s.isMatch('cb', '?a'))
print( s.isMatch('adceb', '*a*b'))
print( s.isMatch('acdcb', 'a*c?b'))