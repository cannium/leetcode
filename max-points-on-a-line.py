# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) == 0:
            return 0
        elif len(points) == 1:
            return 1
        self.same = []
        i = 0
        while(i < len(points)):
            self.slope = {}
            samePoint = 0
            j = i + 1
            while (j < len(points)):
                slope = self.computeSlope(points[i], points[j])
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    samePoint += 1
                else:
                    if self.slope.get(slope, 0) == 0:
                        self.slope[slope] = 1
                    else:
                        self.slope[slope] += 1
                maxSame = 0
                for k, v in self.slope.iteritems():
                    if v > maxSame:
                        maxSame = v
                self.same.append(maxSame + samePoint)
                j += 1
            i += 1
        return max(self.same) + 1


    def computeSlope(self, pointi, pointj):
        deltay = pointi.y - pointj.y
        deltax = pointi.x - pointj.x
        if deltax == 0:
            slope = float('inf')
        else:
            slope = 1.0 * deltay / deltax

        return slope


