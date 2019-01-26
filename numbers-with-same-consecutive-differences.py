def f(n, K, first):
    ans = []
    for i in range(10):
        if abs(i-first) == K:
            if n == 1:
                ans.append(i)
            else:
                vals = f(n-1, K, i)
                for v in vals:
                    ans.append(i * (10**(n-1)) + v)
    return ans

class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [0,1,2,3,4,5,6,7,8,9]
        ans = []
        for i in range(1, 10):
            vals = f(N-1, K, i)
            for v in vals:
                ans.append(i * (10**(N-1)) + v)
        return ans