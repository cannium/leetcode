from typing import List
import sys

def find(parent, i):
    if parent[i] == -1:
        return i
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, i, j):
    pi = find(parent, i)
    pj = find(parent, j)
    parent[pi] = pj
    parent[i] = pj
    parent[j] = pj

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        random.shuffle(connections)
        parent = [-1] * n
        useless = 0
        for x, y in connections:
            if find(parent, x) == find(parent, y):
                useless += 1
                continue
            union(parent, x, y)
        ans = 0
        for i in range(1, n):
            if find(parent, i) != find(parent, 0):
                if useless > 0:
                    useless -= 1
                    ans += 1
                    union(parent, i, 0)
                else:
                    return -1
        return ans

s = Solution()
print(s.makeConnected(4, [[0,1],[0,2],[1,2]]))
#print(s.makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
#print(s.makeConnected(6, [[0,1],[0,2],[0,3],[1,2]]))
#print(s.makeConnected(5, [[0,1],[0,2],[3,4],[2,3]]))