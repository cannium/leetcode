# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        if len(A) == 0 or len(B) == 0:
            return []
        i, j = 0, 0
        ans = []
        while i < len(A) and j < len(B):
            if A[i].end < B[j].start:
                i += 1
                continue
            if B[j].end < A[i].start:
                j += 1
                continue
            ans.append([max(A[i].start,B[j].start), min(A[i].end, B[j].end)])
            if A[i].end == B[j].end:
                i += 1
                j += 1
                continue
            if A[i].end > B[j].end:
                j += 1
            else:
                i += 1
        return ans
