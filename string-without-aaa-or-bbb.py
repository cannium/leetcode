class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        ans = ''
        last = None
        while A > 0 and B > 0:
            if A/B >= 2:
                if last is None or last == 'b':
                    ans += 'aa'
                    last = 'a'
                    A -= 2
                else:
                    ans += 'b'
                    last = 'b'
                    B -= 1
            elif B/A >= 2:
                if last is None or last == 'a':
                    ans += 'bb'
                    last = 'b'
                    B -= 2
                else:
                    ans += 'a'
                    last = 'a'
                    A -= 1
            elif A > B:
                if last is None or last == 'b':
                    ans += 'a'
                    last = 'a'
                    A -= 1
                else:
                    ans += 'b'
                    last = 'b'
                    B -= 1
            else:
                if last is None or last == 'a':
                    ans += 'b'
                    last = 'b'
                    B -= 1
                else:
                    ans += 'a'
                    last = 'a'
                    A -= 1
        if A > 0:
            ans += 'a' * A
        if B > 0:
            ans += 'b' * B
        return ans

