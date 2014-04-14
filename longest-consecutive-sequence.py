class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num.sort()
        longest = 1
        current = 1
        for i in range(1, len(num)):
            if num[i] == num[i-1] + 1:
                current += 1
            elif num[i] == num[i-1]:
                pass
            else:
                current = 1

            if current > longest:
                longest = current

        return longest


s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])
