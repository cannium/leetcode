# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        mid = (i+j)/2
        while j-i > 1:
            mid = (i+j)/2
            #print mid
            if isBadVersion(mid):
                i,j = i, mid-1
            else:
                i,j = mid+1, j
        if i > j:
            i, j = j, i
        badi = isBadVersion(i)
        badj = isBadVersion(j)
        if not badi and badj:
            return j
        if not badj:
            return j+1
        if badi:
            return i
                
