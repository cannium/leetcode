def product(memo, i, j, nums):
    if i == j:
        return nums[i]
    if (i, j) in memo:
        return memo[(i, j)]
    ans = product(memo, i+1, j, nums) * nums[i]
    memo[(i,j)] = ans
    return ans

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        memo = {}
        for i in range(0, len(nums)):
            if i == 0:
                dp[i] = nums[i]
                continue
            ans = max(dp[i-1], nums[i])
            for j in range(0, i):
                ans = max(ans, product(memo, j, i, nums))
            dp[i] = ans
        return dp[-1]