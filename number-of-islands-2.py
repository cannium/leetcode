def find_parent(row, col, table):
    while table[row][col] is not None:
        newrow, newcol = table[row][col]
        if newrow == row and newcol == col:
            return row, col
        row, col = newrow, newcol
    return (row, col)

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent_table = [[None for i in range(n)] for i in range(m)]
        grid = [[0 for i in range(n)] for i in range(m)]
        count = 0
        ans = []
        for row, col in positions:
            count += 1
            grid[row][col] = 1
            for di in [[0,1],[0,-1],[-1,0],[1,0]]:
                newrow, newcol = row+di[0], col+di[1]
                if 0 <= newrow and newrow < m and 0 <= newcol and newcol < n and grid[newrow][newcol] == 1:
                    p = find_parent(row, col, parent_table)
                    newp = find_parent(newrow, newcol, parent_table)
                    #print row, col, p, newp
                    if p != newp:
                        count -= 1
                        parent_table[p[0]][p[1]] = newp
            ans.append(count)
        return ans
