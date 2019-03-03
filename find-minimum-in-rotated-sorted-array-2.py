def findp(nums, i, j):
    if j - i < 4:
        m = i
        for k in range(i, j+1):
            if nums[k] < nums[m]:
                m = k
        return nums[m]
    mid = i + (j-i)/2
    if nums[mid] > nums[j]:
        return findp(nums, mid+1, j)
    if nums[mid] == nums[j]:
        return min(findp(nums, i, mid), findp(nums, mid+1, j))
    return findp(nums, i, mid)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0]
        if nums[len(nums)-1] > nums[0]:
            return nums[0]
        return findp(nums, 0, len(nums)-1)
