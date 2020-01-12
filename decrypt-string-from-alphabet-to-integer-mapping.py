def n2c(n):
    n = int(n)
    x = n - 1 + ord('a')
    return str(chr(x))

class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        i = 0
        while True:
            if i >= len(s):
                break
            if i+2 < len(s) and s[i+2] == '#':
                n = s[i:i+2]
                c = n2c(n)
                ans += c
                i += 3
                continue
            n = s[i]
            c = n2c(n)
            ans += c
            i += 1
        return ans
        

s = Solution()
print s.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")
print s.freqAlphabets("10#11#12")