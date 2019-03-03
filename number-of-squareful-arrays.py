import math

def isSquare(n):
    sr = math.sqrt(n) 
    return ((sr - math.floor(sr)) == 0) 

class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = {}
        pair = {}
        for i in range(len(A)):
            if A[i] in count:
                count[A[i]] += 1
            else:
                count[A[i]] = 1
            for j in range(i+1, len(A)):
                if isSquare(A[i] + A[j]):
                    if A[i] in pair:
                        pair[A[i]][A[j]] = 1
                    else:
                        pair[A[i]] = {A[j]: 1}
                    if A[j] in pair:
                        pair[A[j]][A[i]] = 1
                    else:
                        pair[A[j]] = {A[i]: 1}
        l = [-1] * len(A)
        ans = [0]
        def dfs(i):
            if i >= len(A):
                ans[0] += 1
                return
            if i == 0:
                for x in count.keys():
                    if x not in pair:
                        continue
                    l[0] = x
                    count[x] -= 1
                    dfs(i+1)
                    count[x] += 1
                    l[0] = -1
            else:
                for x in pair[l[i-1]].keys():
                    if count[x] <= 0:
                        continue
                    l[i] = x
                    count[x] -= 1
                    dfs(i+1)
                    count[x] += 1
                    l[i] = -1
        dfs(0)
        return ans[0]

s = Solution()
print s.numSquarefulPerms([1,8,17])
print s.numSquarefulPerms([1,17,8])
print s.numSquarefulPerms([2,2,2])
print s.numSquarefulPerms([1,1])