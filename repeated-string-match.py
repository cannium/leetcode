class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        d = {}
        for c in A:
            d[c] = True
        for c in B:
            if c not in d:
                return -1
        lenA = len(A)
        lenB = len(B)
        n = (lenB + lenA - 1)/ lenA
        if B in A * n:
            return n
        if B in A * (n+1):
            return n+1
        return -1
