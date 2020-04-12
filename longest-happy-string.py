class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        ans = ''
        prev = None
        while a > 0 or b > 0 or c > 0:
            if len(ans) != 0:
                prev = ans[-1]
            #print a,b,c,prev
            if a != 0 and b == 0 and c == 0:
                if prev == 'a':
                    break
                n = min(2, a)
                ans += 'a' * n
                break
            elif b != 0 and a == 0 and c == 0:
                if prev == 'b':
                    break
                n = min(2, b)
                ans += 'b' * n
                break
            elif c != 0 and a == 0 and b == 0:
                if prev == 'c':
                    break
                n = min(2, c)
                ans += 'c' * n
                break
            elif a > 2 * (b+c):
                if prev != 'a':
                    ans += 'aa'
                    a -= 2
                    continue
                else:
                    if b == 0 and c == 0:
                        break
                    if b > c:
                        ans += 'b'
                        b -= 1
                        continue
                    else:
                        ans += 'c'
                        c -= 1
                        continue
            elif b > 2 * (a+c):
                if prev != 'b':
                    ans += 'bb'
                    b -= 2
                    continue
                else:
                    if a == 0 and c == 0:
                        break
                    if a > c:
                        ans += 'a'
                        a -= 1
                        continue
                    else:
                        ans += 'c'
                        c -= 1
                        continue
            elif c > 2 * (a+b):
                if prev != 'c':
                    ans += 'cc'
                    c -= 2
                    continue
                else:
                    if a == 0 and b == 0:
                        break
                    if a > b:
                        ans += 'a'
                        a -= 1
                        continue
                    else:
                        ans += 'b'
                        b -= 1
                        continue
            elif a > b and a > c:
                if prev != 'a':
                    ans += 'a'
                    a -= 1
                    continue
                else:
                    if b == 0 and c == 0:
                        break
                    if b > c:
                        ans += 'b'
                        b -= 1
                        continue
                    else:
                        ans += 'c'
                        c -= 1
                        continue
            elif b > a and b > c:
                if prev != 'b':
                    ans += 'b'
                    b -= 1
                    continue
                else:
                    if a == 0 and c == 0:
                        break
                    if a > c:
                        ans += 'a'
                        a -= 1
                        continue
                    else:
                        ans += 'c'
                        c -= 1
                        continue
            elif c > a and c > b:
                if prev != 'c':
                    ans += 'c'
                    c -= 1
                    continue
                else:
                    if a == 0 and b == 0:
                        break
                    if a > b:
                        ans += 'a'
                        a -= 1
                        continue
                    else:
                        ans += 'b'
                        b -= 1
                        continue
            else:
                if prev != 'a' and a != 0:
                    ans += 'a'
                    a -= 1
                    continue
                elif prev != 'b' and b != 0:
                    ans += 'b'
                    b -= 1
                    continue
                elif prev != 'c' and c != 0:
                    ans += 'c'
                    c -= 1
                    continue
                else:
                    break
        return ans


                    
s = Solution()
# print s.longestDiverseString(1,1,7)
# print s.longestDiverseString(2,2,1)
# print s.longestDiverseString(7,1,0)
print s.longestDiverseString(3,3,1)