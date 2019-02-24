def findR(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                return (i,j)
            
def findp(rx, ry, dx, dy, board):
    x, y = rx, ry
    while True:
        x, y = x + dx, y + dy
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            return 0
        if board[x][y] == 'B':
            return 0
        if board[x][y] == 'p':
            return 1
    return 0

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rx, ry = findR(board)
        ans = 0
        ans += findp(rx, ry, 0, 1, board)
        ans += findp(rx, ry, 1, 0, board)
        ans += findp(rx, ry, 0, -1, board)
        ans += findp(rx, ry, -1, 0, board)
        return ans

                
