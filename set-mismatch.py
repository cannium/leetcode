class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = [0] * (len(nums)+1)
        for x in nums:
            m[x] += 1
        miss, twice = None, None
        for i in range(1, len(m)):
            if m[i] == 0:
                miss = i
            if m[i] == 2:
                twice = i
        return [twice, miss]
        
