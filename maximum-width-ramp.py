class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = {}
        l = []
        for i in xrange(len(A)):
            if A[i] in d:
                d[A[i]][1] = i
            else:
                d[A[i]] = [i, i]
                l.append(A[i])
        l = sorted(l)
        ret = 0
        #print l
        #print d
        ii = 50000
        for i in range(len(l)):
            n = l[i]
            dd = d[n]
            ret = max(ret, dd[1] - dd[0], dd[1]-ii)
            ii = min(ii, dd[0])
        return ret

        
