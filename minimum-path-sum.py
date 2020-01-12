class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cost = []
        width = 0
        for arr in grid:
            width = len(arr)
            cost.append([0] * len(arr))
        height = len(cost)
        for i in range(0, width):
            for j in range(0, height):
                if i == 0 and j == 0:
                    cost[0][0] = grid[0][0]
                elif i == 0:
                    cost[j][i] = cost[j-1][i] + grid[j][i]
                elif j == 0:
                    cost[j][i] = cost[j][i-1] + grid[j][i]
                else:
                    cost[j][i] = min(cost[j-1][i], cost[j][i-1])+grid[j][i]
        #print cost
        return cost[height-1][width-1]
