def smaller(nums, i):
    ans = 0
    for x in nums:
        if x <= i:
            ans += 1
    return ans

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1
        r = len(nums)
        while l < r:
            mid = (l+r)/2
            s = smaller(nums, mid)
            if s <= mid:
                l = mid + 1
            else:
                r = mid
        return l

