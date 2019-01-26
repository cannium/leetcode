def parent(union, x):
    if union[x] == -1:
        return x
    return parent(union, union[x])

def u(union, x, y):
    xset = parent(union, x)
    yset = parent(union, y)
    union[xset] = yset

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        union = [-1] * n
        for i, j in edges:
            pi = parent(union, i)
            pj = parent(union, j)
            if pi == pj:
                return False
            u(union, i, j)
        if len(edges) != n - 1:
            return False
        return True
