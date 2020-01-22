
class Solution:
    def calculateMinimumHP(self, dungeon):
        if len(dungeon) == 0:
            return 0
        dp = [[None for x in range(0, len(dungeon[0]))] for x in range(0, len(dungeon))]
        for i in range(len(dungeon)-1, -1, -1):
            for j in range(len(dungeon[0])-1, -1, -1):
                if i == len(dungeon)-1 and j == len(dungeon[0])-1:
                    dp[i][j] = max(1, 1-dungeon[i][j])
                    continue
                need1, need2 = float('inf'), float('inf')
                if i+1 < len(dungeon):
                    need1 = max(dp[i+1][j] - dungeon[i][j], 1)
                if j+1 < len(dungeon[0]):
                    need2 = max(dp[i][j+1] - dungeon[i][j], 1)
                dp[i][j] = min(need1, need2)
        #print(dp)
        return dp[0][0]
    
s = Solution()
s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])
s.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]])
s.calculateMinimumHP([[0,-3]])
s.calculateMinimumHP([[0,-5],[0,0]])




        