def test(memo, s, left, right):
    if left > right:
        return 0
    if left == right:
        return 1 << (ord(s[left]) - ord('a'))
    return memo[right+1] ^ memo[left]

def count(x):
    n = 0
    while(x):
        n += x & 1
        x >>= 1
    return n

class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        ans = []
        memo = [0] * len(s)
        d = 0
        for i in range(len(s)):
            memo[i] = d ^ (1 << (ord(s[i]) - ord('a')))
            d = memo[i]
        memo = [0] + memo + [d]
        #print memo

        for q in queries:
            d = test(memo, s, q[0], q[1])
            if q[2] >= (count(d)/2):
                ans.append(True)
            else:
                ans.append(False)
        return ans


s = Solution()
print s.canMakePaliQueries('abcda', 
[[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]])
print count(7)