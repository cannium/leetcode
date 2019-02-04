class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.v = v
        self.len = 0
        for l in v:
            self.len += len(l)
        self.i = 0
        self.l_i = 0
        if len(v) > 0:
            self.cur = v[0]
        else:
            self.cur = []
        self.cur_i = 0

    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        if self.cur_i < len(self.cur):
            ans = self.cur[self.cur_i]
            self.cur_i += 1
            return ans
        self.l_i += 1
        while len(self.v[self.l_i]) == 0:
            self.l_i += 1
        self.cur = self.v[self.l_i]
        self.cur_i = 0
        ans = self.cur[self.cur_i]
        self.cur_i += 1
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < self.len
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
