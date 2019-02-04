def lower_bound(array, first, last, value):
    while first < last:
        mid = first + (last - first) // 2
        if array[mid] < value:
            first = mid + 1
        else:
            last = mid
    return first

def ind(i, days, x):
    if days[i] == x:
        return i
    return i-1

def di(i, days):
    if i == -1:
        return 0
    return days[i]

class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        ans = 0
        dc = [0] * 366
        for i in range(len(days)):
            d = days[i]
            c1, c7, c30 = float('inf'),float('inf'),float('inf')
            i30 = lower_bound(days, 0, i, d - 30)
            #print 'i30', i, i30
            i30 = ind(i30, days, d-30)
            di30 = di(i30, days)
            c30 = dc[di30] + costs[2]
            i7 = lower_bound(days, 0, i, d - 7)
            i7 = ind(i7, days, d-7)
            di7 = di(i7, days)
            c7 = dc[di7] + costs[1]
            i1 = lower_bound(days, 0, i, d - 1)
            i1 = ind(i1, days, d-1)
            di1 = di(i1, days)
            c1 = dc[di1] + costs[0]
            #print d, c1, c7, c30
            dc[d] = min(c1,c7,c30)
        #for i in range(len(dc)):
        #    if dc[i] != 0:
        #        print i, dc[i]
        return dc[days[len(days)-1]]

