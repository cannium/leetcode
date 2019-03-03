def cmp(ix, iy):
    if ix[0] == iy[0]:
        return ix[1] - iy[1]
    return ix[0] - iy[0]

class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, cmp = cmp)
        #print intervals
        merged = intervals[:]
        j = 0
        for i in range(len(intervals)):
            if i == 0:
                merged[j] = intervals[i]
                j += 1
                continue
            k = j
            x, y = intervals[i]
            while k-1 >= 0:
                formerx, formery = merged[k-1]
                if formerx <= x and formery >= y:
                    k -= 1
                else:
                    break
            merged[k] = [x,y]
            j = k+1
        #print merged
        s = []
        i = None
        for x, y in merged[:j]:
            if i is None:
                s += [y-1, y]
                i = 1
                continue
            already = 0
            j = i
            while j >= 0:
                if s[j] >= x:
                    already += 1
                else:
                    break
                j-=1
            if already == 2:
                continue
            if already == 1:
                s.append(y)
                i += 1
                continue
            s += [y-1, y]
            i += 2
        #print s
        return len(s)
                
