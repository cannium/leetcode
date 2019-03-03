def bs(nums, i, j, x):
    while i < j:
        mid = i + (j-i)/2
        if nums[mid] < x:
            i = mid + 1
        else:
            j = mid
    return i

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum2 = nums[i] + nums[j]
                k = bs(nums, j+1, len(nums), sum2)
                #print i, j, k
                if k - 1 - j > 0:
                    ans += (k-j-1)
        return ans
