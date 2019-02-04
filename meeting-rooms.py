# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def cmp(x, y):
    return x.start - y.start

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals = sorted(intervals, cmp=cmp)
        for i in range(1, len(intervals)):
            early = intervals[i-1]
            late = intervals[i]
            if late.start < early.end:
                return False
        return True
            
