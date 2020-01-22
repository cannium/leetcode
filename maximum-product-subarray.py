from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        maxPositive = None
        maxNegative = None
        for i in range(0, len(nums)):
            n = nums[i]
            ans = max(ans, n)
            if n == 0:
                maxPositive = None
                maxNegative = None
                continue
            if n > 0:
                if maxPositive:
                    maxPositive = maxPositive * n
                    ans = max(ans, maxPositive)
                else:
                    maxPositive = n
                if maxNegative:
                    maxNegative = maxNegative * n
            if n < 0:
                if maxPositive:
                    negative = maxPositive * n
                    maxPositive = None
                else:
                    negative = n
                if maxNegative:
                    maxPositive = maxNegative * n
                    ans = max(ans, maxPositive)
                maxNegative = negative
        return ans

s = Solution()
# print(s.maxProduct([-1, 2, 3, -5]))
print(s.maxProduct([2,3,-2,4]))