import math

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(start, path, target):
            #print start, path, target
            if len(path) > 0:
                ans.append(path+[target])
            for i in range(start, int(math.sqrt(target))+1):
                if target % i == 0:
                    p = path[:]
                    p.append(i)
                    dfs(i, p, target/i)
        dfs(2, [], n)
        return ans
