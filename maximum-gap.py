import math

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return abs(nums[0]-nums[1])
        l, r = float('inf'), float('-inf')
        for n in nums:
            if n > r:
                r = n
            if n < l:
                l = n
        size = max(1, (r-l)/len(nums))
        mins = [-1] * ((r-l)/size+1)
        maxs = [-1] * ((r-l)/size+1)
        for n in nums:
            slot = (n-l) / size
            if mins[slot] == -1:
                mins[slot] = n
            if maxs[slot] == -1:
                maxs[slot] = n
            if n < mins[slot]:
                mins[slot] = n
            if n > maxs[slot]:
                maxs[slot] = n
        ans = 0
        #print mins
        #print maxs
        now = -1
        for i in range(0, len(mins)):
            if now == -1:
                now = maxs[i]
                continue
            if mins[i] - now > ans:
                ans = mins[i] - now
            if maxs[i] != -1:
                now = maxs[i]
        return ans
