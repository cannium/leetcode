class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = [0] * len(nums)
        d = {}
        for i in range(len(nums)):
            if i == 0:
                sums[i] = nums[0]
            else:
                sums[i] = sums[i-1] + nums[i]
            if sums[i] not in d:
                d[sums[i]] = i
        ans = 0
        for i in range(len(sums)):
            if sums[i] == k:
                ans = i + 1
                continue
            need = sums[i] - k
            if need in d:
                if i - d[need] > ans:
                    ans = i - d[need]
        return ans

