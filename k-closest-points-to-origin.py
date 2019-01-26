def compare(x, y):
    return x[0]*x[0] + x[1]*x[1] - y[0]*y[0] - y[1]*y[1]

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if k >= len(points):
            return points
        points = sorted(points, cmp=compare)
        return points[:k]