def dfs(grid, visit, gold, i, j):
    #print i, j, gold, visit
    if visit[i][j]:
        return gold
    visit[i][j] = True
    collect = gold + grid[i][j]
    ans = collect
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        ni = i + dx
        nj = j + dy
        if ni < 0 or ni >= len(grid):
            continue
        if nj < 0 or nj >= len(grid[0]):
            continue
        if grid[ni][nj] == 0:
            continue
        if visit[ni][nj]:
            continue
        g = dfs(grid, visit, collect, ni, nj)
        ans = max(ans, g)
    visit[i][j] = False
    return ans

class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visit = [ [False] * len(grid[0]) for i in range(len(grid))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print '========'
                if grid[i][j] != 0:
                    g = dfs(grid, visit, 0, i, j)
                    ans = max(g, ans)
        return ans


s = Solution()
print s.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])