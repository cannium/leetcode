direction = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def check(grid):
    for line in grid:
        if 0 in line:
            return False
    return True

def dfs(i, j, grid, ans):
    for dx, dy in direction:
        x, y = i + dx, j + dy
        if x < 0 or x >= len(grid):
            continue
        if y < 0 or y >= len(grid[0]):
            continue
        if grid[x][y] == 2:
            if check(grid):
                ans[0] += 1
                continue
        if grid[x][y] != 0:
            continue
        grid[x][y] = 3
        dfs(x, y, grid, ans)
        grid[x][y] = 0


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                return i, j

class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i, j = find_start(grid)
        ans = [0]
        dfs(i, j, grid, ans)
        return ans[0]


s = Solution()
print s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
print s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])
print s.uniquePathsIII([[0,1],[2,0]])