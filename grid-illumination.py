def lit(qx, qy, diag, diag2, row, col):
    d = qx - qy
    if d in diag:
        return 1
    d2 = qy + qx
    if d2 in diag2:
        return 1
    if qx in row:
        return 1
    if qy in col:
        return 1
    return 0

direction = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

def turnOff(qx, qy, board, N):
    ans = []
    for dx, dy in direction:
        x, y = qx + dx, qy + dy
        if x < 0 or x >= N:
            continue
        if y < 0 or y >= N:
            continue
        if (x, y) in board:
            ans.append((x,y))
    return ans
    
    

class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        board = {}
        diag = {}
        diag2 = {}
        row = {}
        col = {}
        for l in lamps:
            l = tuple(l)
            x, y = l
            board[l] = 1
            d = x - y
            if d in diag:
                diag[d][l] = 1
            else:
                diag[d] = {l: 1}
            d2 = y + x
            if d2 in diag2:
                diag2[d2][l] = 1
            else:
                diag2[d2] = {l: 1}
            if x in row:
                row[x][l] = 1
            else:
                row[x] = {l: 1}
            if y in col:
                col[y][l] = 1
            else:
                col[y] = {l: 1}
        ans = []
        for qx, qy in queries:
            ans.append(lit(qx, qy, diag, diag2, row, col))
            lights = turnOff(qx, qy, board, N)
            for l in lights:
                del(board[l])
                x, y = l
                d = x - y
                if d in diag:
                    if l in diag[d]:
                        del(diag[d][l])
                        if len(diag[d]) == 0:
                            del(diag[d])
                d2 = y + x
                if d2 in diag2:
                    if l in diag2[d2]:
                        del(diag2[d2][l])
                        if len(diag2[d2]) == 0:
                            del(diag2[d2])
                if x in row:
                    if l in row[x]:
                        del(row[x][l])
                        if len(row[x]) == 0:
                            del(row[x])
                if y in col:
                    if l in col[y]:
                        del(col[y][l])
                        if len(col[y]) == 0:
                            del(col[y])
        return ans
            
        
