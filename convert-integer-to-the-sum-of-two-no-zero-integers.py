class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for x in range(1, n):
            if '0' in str(x):
                continue
            y = n - x
            if '0' not in str(y):
                return [x, y]

s = Solution()
print(s.getNoZeroIntegers(10000))