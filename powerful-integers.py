class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if x == 1 and y == 1:
            if bound >= 2:
                return [2]
            else:
                return []
        
        ans = []
        if x == 1:
            x, y = y, x
        if y == 1:
            xx = 1
            for i in xrange(100000):
                if 1 + xx <= bound:
                    ans.append(1+xx)
                else:
                    break
                xx = xx * x
            return ans
            
        ans = {}
        i = 0
        j = 0
        xx = 1
        for i in xrange(100000):
            yy = 1
            if xx + yy > bound:
                break
            for j in xrange(100000):
                if xx + yy <= bound:
                    ans[xx+yy] = 1
                else:
                    break
                yy = yy * y
            xx = xx * x
        ret = []
        for k in ans:
            ret.append(k)
        return ret
            

t = Solution()
print t.powerfulIntegers(2,3,10)

print t.powerfulIntegers(3,5,15)

print t.powerfulIntegers(1,1,1)
print t.powerfulIntegers(1,4,10000)
