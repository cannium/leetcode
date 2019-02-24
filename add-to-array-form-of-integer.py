class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        ten = 10 ** (len(A)-1)
        a = 0
        for d in A:
            a += d * ten
            ten = ten/10
        ans = a + K
        return [int(x) for x in str(ans)]
        
