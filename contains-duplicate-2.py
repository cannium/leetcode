from collections import defaultdict
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = defaultdict(lambda:0)
        if k+1 >= len(nums):
            for n in nums:
                d[n] += 1
                if d[n] > 1:
                    return True
            return False
        for i in range(k+1):
            d[nums[i]] += 1
            if d[nums[i]] > 1:
                return True
        for i in range(k+1, len(nums)):
            d[nums[i-k-1]] -= 1
            d[nums[i]] += 1
            if d[nums[i]] > 1:
                return True
        return False
