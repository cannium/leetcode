class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        cur = 0
        for v in A:
            if v % 2 == 0:
                cur += v
        for v, i in queries:
            if A[i] % 2 == 0:
                cur -= A[i]
            A[i] += v
            if A[i] % 2 == 0:
                cur += A[i]
            ans.append(cur)
        return ans
