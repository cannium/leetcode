class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['0','1','8']
        nn = 1
        l = ['0','1','8']
        if n % 2 == 0:
            nn = 2
            l = ["00","11","69","88","96"]
        while nn < n:
            new_l = []
            for c in l:
                new_l += ['1'+c+'1', '6'+c+'9', '8'+c+'8', '9'+c+'6', '0'+c+'0']
            nn += 2
            l = new_l
        ans = []
        for c in l:
            if c[0] != '0':
                ans.append(c)
        return ans
