class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)
        mul = 1
        for i in range(1, len(nums)):
            mul = mul * nums[i-1]
            ans[i] = mul
        mul = 1
        for i in range(len(nums)-2, -1, -1):
            mul = mul * nums[i+1]
            ans[i] = ans[i] * mul
        return ans
