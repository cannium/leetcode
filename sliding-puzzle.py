from collections import defaultdict

def b2i(board):
    ans = 0
    for i in range(2):
        for j in range(3):
            ans = 10 * ans + board[i][j]
    return ans

def i2b(x, board):
    zero = (-1, -1)
    for i in range(1, -1, -1):
        for j in range(2, -1, -1):
            r = x % 10
            board[i][j] = r
            x = x / 10
            if r == 0:
                zero = (i, j)
    return zero

direction = [
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]
]

def next_x(zero, board):
    ans = []
    i, j = zero
    for dx, dy in direction:
        x, y = i + dx, j + dy
        if x < 0 or x >= 2:
            continue
        if y < 0 or y >= 3:
            continue
        board[i][j], board[x][y] = board[x][y], board[i][j]
        ans.append(b2i(board))
        board[i][j], board[x][y] = board[x][y], board[i][j]
    return ans

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        visited = defaultdict(lambda: False)
        start = b2i(board)
        if start == 123450:
            return 0
        q = [start]
        step = 0
        while len(q) > 0:
            next_q = []
            for x in q:
                visited[x] = True
                zero = i2b(x, board)
                nexts = next_x(zero, board)
                for n in nexts:
                    if visited[n]:
                        continue
                    if n == 123450:
                        return step + 1
                    next_q.append(n)
            q = next_q
            step += 1
        return -1 


s = Solution()
print s.slidingPuzzle([[1,2,3],[4,0,5]])
print s.slidingPuzzle([[1,2,3],[5,4,0]])
print s.slidingPuzzle([[4,1,2],[5,0,3]])
print s.slidingPuzzle([[3,2,4],[1,5,0]])
