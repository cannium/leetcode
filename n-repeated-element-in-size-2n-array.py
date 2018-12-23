class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = {}
        for x in A:
            if x in d:
                return x
            d[x] = True
