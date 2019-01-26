from collections import OrderedDict

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.od = OrderedDict()
        self.total = 0
        self.last = 300
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if timestamp < self.last - 299:
            return
        if timestamp > self.last:
            self.last = timestamp
            for t in self.od:
                if t < self.last - 299:
                    self.total -= self.od[t]
                    del(self.od[t])
                else:
                    break
            
        if timestamp in self.od:
            self.od[timestamp] += 1
        else:
            self.od[timestamp] = 1
        self.total += 1


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        if timestamp < self.last - 299:
            return 0
        if timestamp > self.last:
            self.last = timestamp
            for t in self.od:
                if t < self.last - 299:
                    self.total -= self.od[t]
                    del(self.od[t])
                else:
                    break
        return self.total
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
