from typing import List

def previousMax(edges, currentRow):
    maxRec = 0
    for row_i, col_l, col_r in edges:
        maxRec = max(
            maxRec, 
            (col_r - col_l + 1) * (currentRow - row_i)
        )
    return maxRec

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        maxRec = 0
        edges = [] # [(row_i, col_l, col_r)]
        for i in range(0, len(matrix)):
            #print(i, edges)
            maxRec = max(maxRec, previousMax(edges, i))

            row = matrix[i]
            lastOne = None
            ones = [] # [(col_l, col_r)]
            for j in range(0, len(row)):
                if row[j] == '1':
                    if lastOne is None:
                        lastOne = j
                else:
                    if lastOne is not None:
                        ones.append((lastOne, j-1))
                        lastOne = None
            if lastOne is not None:
                ones.append((lastOne, len(row)-1))

            nextEdgesMap = {}
            for row_i, col_l, col_r in edges:
                for l, r in ones:
                    intersec_l = max(col_l, l)
                    intersec_r = min(col_r, r)
                    if intersec_l > intersec_r:
                        continue
                    ii = row_i
                    if (intersec_l, intersec_r) in nextEdgesMap:
                        ii = min(row_i, nextEdgesMap[(intersec_l, intersec_r)])
                    nextEdgesMap[(intersec_l, intersec_r)] = ii
            for l, r in ones:
                if (l, r) not in nextEdgesMap:
                    nextEdgesMap[(l, r)] = i
                
            nextEdges = []
            for l, r in nextEdgesMap:
                row_i = nextEdgesMap[(l, r)]
                nextEdges.append((row_i, l, r))
            edges = nextEdges
        maxRec = max(maxRec, previousMax(edges, len(matrix)))
        return maxRec
            

s = Solution()
print(s.maximalRectangle([["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]
))
#print(s.maximalRectangle([["1"],["1"],["0"],["1"],["1"],["1"],["0"],["1"],["1"],["0"],["0"],["1"],["1"],["1"],["1"],["1"],["0"],["0"],["1"],["1"],["0"],["1"],["0"],["1"],["1"],["0"],["1"],["1"],["1"],["1"],["1"],["1"],["0"],["1"],["1"],["1"],["0"],["1"],["0"],["1"],["1"],["1"],["1"],["0"],["1"],["1"],["1"],["1"],["0"],["0"],["1"],["0"],["1"],["0"],["1"],["1"],["0"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["0"],["1"],["1"],["1"],["1"],["1"],["0"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["0"],["1"],["1"],["1"],["1"],["1"],["1"],["1"],["1"]]
#))
#print(s.maximalRectangle([["0","1","1","1","1","1","0","1","1","1","1","1","0","1","0","1","1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0","0","0","1","1","0","1","1","1","0","1","1","1","1","0","0","1","1","1","0","0","0","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","0","1","1","1","1","0","1","1","1","1","1","1","1","1","0","0","1","0","1","0","1","0"]]))