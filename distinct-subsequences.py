def char2loc(s):
    d = {}
    for i in range(0, len(s)):
        c = s[i]
        if c in d:
            d[c].append(i)
        else:
            d[c] = [i]
    return d

def dp(memo, sChar2Loc, i, j, s, t):
    # print(i, j)
    if i < 1 or j < 1:
        return 0
    if i < j:
        return 0
    if i == j:
        if s[:i] == t[:j]:
            return 1
        else:
            return 0
    if (i, j) in memo:
        return memo[(i, j)]
    ans = 0
    if j == 1:
        ct = t[0]
        for loc in sChar2Loc[ct]:
            if loc < i:
                ans += 1
        memo[(i,j)] = ans
        return ans
    ct = t[j-1]
    for loc in sChar2Loc[ct]:
        if loc < i:
            ans += dp(memo, sChar2Loc, loc, j-1, s, t)
        else:
            break
    memo[(i,j)] = ans
    return ans

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sChar2Loc = char2loc(s)
        # print(sChar2Loc)
        memo = {}
        # dp on s[:i] and t[:j]
        return dp(memo, sChar2Loc, len(s), len(t), s, t)

s = Solution()
print(s.numDistinct("rabbbit", "rabbit"))