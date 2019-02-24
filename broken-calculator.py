class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        count = 0
        while Y > X:
            count += 1
            if Y % 2 == 0:
                Y = Y >> 1
            else:
                Y += 1
        return X - Y + count
