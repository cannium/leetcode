# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def compareInterval(x, y):
    if x.start == y.start:
        return x.end - y.end
    return x.start - y.start

def findRoom(rooms, interval):
    for room in rooms:
        l, r = 0, len(room)
        while l < r:
            mid = l + (r-l)/2
            if room[mid].start < interval.start:
                l = mid + 1
            else:
                r = mid
        if interval.start >= room[l-1].end:
            if l >= len(room) or interval.end <= room[l].start:
                room.insert(l, interval)
                return True
    return False

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        rooms = []
        intervals = sorted(intervals, cmp=compareInterval)
        for i in intervals:
            found = findRoom(rooms, i)
            if not found:
                rooms.append([i])
        return len(rooms)
