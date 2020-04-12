def calc(i, values, m, total):
    if i >= len(values):
        return 0
    if i == len(values) - 1:
        return values[i]
    if i in m:
        return m[i]
    compare = [total - calc(i+1, values, m, total-values[i]),]
    if i+1 < len(values):
        a = total - calc(i+2, values, m, total-values[i]-values[i+1])
        compare.append(a)
    if i+2 < len(values):
        a = total - calc(i+3, values, m, total-values[i]-values[i+1]-values[i+2])
        compare.append(a)
    m[i] = max(compare)
    return max(compare)


class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        m = {}
        total = sum(stoneValue)
        alice = calc(0, stoneValue, m, total)
        bob = total - alice
        #print alice, bob, m
        if alice > bob:
            return 'Alice'
        elif alice < bob:
            return 'Bob'
        else:
            return 'Tie'


s = Solution()
print s.stoneGameIII([1,2,3,7])
print s.stoneGameIII([1,2,3,-9])
print s.stoneGameIII([1,2,3,6])
print s.stoneGameIII([1,2,3,-1,-2,-3,7])
print s.stoneGameIII([-1,-2,-3])