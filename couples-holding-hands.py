def swap(x, y, loc, row):
    i = loc[x]
    j = loc[y]
    row[i], row[j] = row[j], row[i]
    loc[x] = j
    loc[y] = i
    
def another(x):
    if x/2*2 == x:
        return x/2*2+1
    else:
        return x/2*2

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        loc = {}
        for i in range(len(row)):
            x = row[i]
            loc[x] = i
        ans = 0
        for i in range(0, len(row), 2):
            if row[i]/2 == row[i+1]/2:
                continue
            x = row[i]
            another_x = another(x)
            y = row[i+1]
            swap(y, another_x, loc, row)
            ans += 1
        return ans
