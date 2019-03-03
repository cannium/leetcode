from collections import defaultdict

def dp(s, l, r, memo):
    if l > r:
        return 0
    if l == r:
        return 1
    if (l,r) in memo:
        return memo[(l,r)]
    if s[l] == s[r]:
        ans = dp(s, l+1, r-1, memo) + 2
        memo[(l,r)] = ans
        return ans
    ans = max(dp(s, l+1, r, memo), dp(s, l, r-1, memo))
    memo[(l,r)] = ans
    return ans

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(lambda: [])
        for i in range(len(s)):
            c = s[i]
            d[c].append(i)
        memo = {}
        return dp(s, 0, len(s)-1, memo)
