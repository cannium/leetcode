class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                continue
            if i == 1:
                dp[i] = n
                continue
            dp[i] = max(dp[i-1], n+dp[i-2])
        ans = dp[-1]
        dp = [0] * len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                dp[i] = n
                continue
            if i == 1:
                dp[i] = max(n, dp[0])
                continue
            if i == len(nums) - 1:
                dp[i] = dp[i-1]
                continue
            dp[i] = max(dp[i-1], n+dp[i-2])
        ans = max(ans, dp[-1])
        return ans

s = Solution()
print(s.rob([2,1,1,1]))
print(s.rob([1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]))