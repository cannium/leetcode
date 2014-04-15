class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        dp = [triangle[0]]
        for i in range(1, len(triangle)):
            line = []
            for j in range(len(triangle[i])):
                if j == 0:
                    line.append(dp[i-1][0] + triangle[i][0])
                elif j == len(triangle[i]) - 1:
                    line.append(dp[i-1][j-1] + triangle[i][j])
                else:
                    line.append(min(dp[i-1][j-1] + triangle[i][j],
                                    dp[i-1][j] + triangle[i][j]))
            dp.append(line)
        #print dp
        return min(dp[-1])


tri = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
s = Solution()
print s.minimumTotal(tri)
