class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d1 = {}
        for x in arr:
            if x in d1:
                d1[x] += 1
            else:
                d1[x] = 1
        d2 = {}
        for k in d1:
            v = d1[k]
            if v in d2:
                return False
            else:
                d2[v] = 1
        return True