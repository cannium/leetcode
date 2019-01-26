class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1:
            return 1
        ans = 1
        cur = 1
        sign = None
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                sign = None
                if cur > ans:
                    ans = cur
                cur = 1
            if A[i] > A[i-1]:
                if sign == None or sign == '<':
                    cur += 1
                else:
                    if cur > ans:
                        ans = cur
                    cur = 2
                sign = '>'
            if A[i] < A[i-1]:
                if sign == None or sign == '>':
                    cur += 1
                else:
                    if cur > ans:
                        ans = cur
                    cur = 2
                sign = '<'
        if cur > ans:
            ans = cur
        return ans
                        

s = Solution()
print s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9])
print s.maxTurbulenceSize([4,8,12,16])
print s.maxTurbulenceSize([100])
