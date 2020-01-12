def dp(memo, n):
    if n <= 0:
        return 1
    if n in memo:
        return memo[n]
    ans = 0
    for i in range(0, n):
        l = i
        r = n - i - 1
        ans += dp(memo, l) * dp(memo, r)
    memo[n] = ans
    return ans

class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        return dp(memo, n)

s = Solution()
print(s.numTrees(2))