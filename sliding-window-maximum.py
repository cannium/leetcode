class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        next_bigger = [-1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            next_i = i + 1
            while next_i != -1 and nums[next_i] < nums[i]:
                next_i = next_bigger[next_i]
            next_bigger[i] = next_i
        '''
        print [i for i in range(len(nums))]
        print nums
        print next_bigger
        print last_smaller
        '''  
        last_max = 0
        ans = []
        for i in range(len(nums)):
            if i < k:
                if nums[i] >= nums[last_max]:
                    last_max = i
                continue
            ans.append(nums[last_max])
            if nums[i] >= nums[last_max]:
                last_max = i
                continue
            if last_max > i - k:
                continue
            big_i = next_bigger[i-k]
            if big_i != -1 and big_i <= i:
                last_max = big_i
                continue
            j = i-k+1
            next_i = next_bigger[j]
            if next_i == -1 or next_i > i:
                last_max = j
                continue
            else:
                while True:
                    next_next_i = next_bigger[next_i]
                    if next_next_i != -1 and next_next_i <= i:
                        next_i = next_next_i
                    else:
                        last_max = next_i
                        break
        ans.append(nums[last_max])
        return ans

