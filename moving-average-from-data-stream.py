class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.count = 0
        self.m = [0] * size
        self.next_i = 0
        self.total = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        size = len(self.m)
        self.total -= self.m[self.next_i]
        self.total += val
        self.m[self.next_i] = val
        self.next_i = (self.next_i + 1) % size
        if self.count < size:
            self.count += 1
        return 1. * self.total / self.count
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
