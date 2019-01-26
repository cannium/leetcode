class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = 0
        for i in range(len(A)):
            s = (s + A[i]) % K
            A[i] = s
        count = {}
        ans = 0
        #print A
        for i in A:
            if i % K == 0:
                ans += 1
            if i in count:
                ans += count[i]
                count[i] += 1
            else:
                count[i] = 1
        return ans
            