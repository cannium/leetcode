class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums, reverse=True)
        total = sum(nums)
        cur = 0
        ans = []
        for n in nums:
            cur += n
            ans.append(n)
            if cur > total - cur:
                return ans
        return ans

s = Solution()
print s.minSubsequence([4,3,10,9,8])
print s.minSubsequence([4,4,7,6,7])
print s.minSubsequence([9])