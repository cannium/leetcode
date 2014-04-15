class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            line = []
            for j in range(i+1):
                if j == 0 or j == i:
                    line.append(ans[i-1][0])
                else:
                    line.append(ans[i-1][j-1] + ans[i-1][j])
            ans.append(line)
        return ans
    def getRow(self, rowIndex):
        tri = self.generate(rowIndex + 1)
        return tri[-1]

s = Solution()
print s.generate(3)
print s.getRow(1)
print s.getRow(3)
