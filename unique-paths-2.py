class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        methods = []
        for l in obstacleGrid:
            width = len(l)
            methods.append([0] * width)
        
        for i in range(0, width):
            for j in range(0, height):
                if obstacleGrid[j][i] == 1:
                    methods[j][i] = 0
                    continue
                if i == 0 and j == 0:
                    methods[0][0] = 1
                    continue
                m = 0
                if j-1 >=0 and obstacleGrid[j-1][i] == 0:
                    m += methods[j-1][i]
                if i-1 >=0 and obstacleGrid[j][i-1] == 0:
                    m += methods[j][i-1]
                methods[j][i] = m
        return methods[height-1][width-1]