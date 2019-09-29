def cost(x, y):
    a = ord(x)
    b = ord(y)
    return abs(a-b)

def diff(i, j, acc):
    if i == 0:
        return acc[j]
    return acc[j] - acc[i-1]

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        costs = [0] * len(s)
        acc = [0] * len(s)
        for i in range(len(s)):
            costs[i] = cost(s[i], t[i])
            if i == 0:
                acc[i] = costs[i]
            else:
                acc[i] = acc[i-1] + costs[i]
        ans = 0
        i, j = 0, 0
        #print costs
        #print acc
        while i < len(s) and j < len(s):
            #print i, j
            if i > j:
                j = i
            if i == j:
                if costs[i] > maxCost:
                    i += 1
                    j += 1
                    continue
                else:
                    ans = max(ans, 1)
            if j + 1 >= len(s):
                break
            if diff(i, j+1, acc) <= maxCost:
                j += 1
                ans = max(ans, j-i + 1)
            else:
                i += 1
        return ans



s = Solution()
print s.equalSubstring("krrgw", "zjxss", 19)
print s.equalSubstring("abcd", "bcdf", 3)
print s.equalSubstring("abcd", "cdef", 3)
print s.equalSubstring("abcd", "acde", 0)