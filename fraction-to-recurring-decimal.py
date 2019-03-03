class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        neg = numerator / denominator < 0
        if numerator < 0: 
            numerator = -numerator
        if denominator < 0: 
            denominator = -denominator
        ans = str(numerator / denominator)
        if neg:
            ans = '-' + ans
        if numerator % denominator == 0:
            return ans
        ans += '.'
        remain = numerator % denominator
        s = ''
        loop = True
        remains = {remain: 0}
        i = 0
        split = 0
        while True:
            i += 1
            c = str(remain * 10 / denominator)
            remain = remain * 10 % denominator
            s += c
            if remain in remains:
                split = remains[remain]
                break
            remains[remain] = i
            if remain == 0:
                loop = False
                break
        if loop:
            ans += s[:split] + '(' + s[split:] + ')'
        else:
            ans += s
        return ans
