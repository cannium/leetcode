class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        d = {}
        for i in range(len(A)):
            for j in range(len(A)):
                x = A[i] & A[j]
                if x in d:
                    d[x] += 1
                else:
                    d[x] = 1
        for k in d:
            for x in A:
                if k & x == 0:
                    ans += d[k]
        return ans


s = Solution()
print s.countTriplets([2,1,3])