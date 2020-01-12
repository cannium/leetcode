def calc(memo, i, j, s):
    if i == -1:
        return len(s) - j
    if j == len(s):
        return i + 1
    if (i, j) in memo:
        return memo[(i,j)]
    if s[i] == s[j]:
        ans = calc(memo, i-1, j+1, s)
        memo[(i, j)] = ans
        return ans    
    ans = min(calc(memo, i-1, j, s) + 1, 
              calc(memo, i, j+1, s) + 1)
    memo[(i, j)] = ans
    return ans

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        shortest = len(s) * 2
        memo = {}
        for pivot in range(0, len(s)):
            if pivot+1 < len(s) and s[pivot] == s[pivot+1]:
                shortest = min(shortest, 
                               calc(memo, pivot-1, pivot+2, s),
                               calc(memo, pivot-1, pivot+1, s))
            else:
                shortest = min(shortest, calc(memo, pivot-1, pivot+1, s))
        return shortest

s = Solution()
print s.minInsertions('zzazz')
print s.minInsertions('mbadm')
print s.minInsertions('leetcode')
print s.minInsertions('g')
print s.minInsertions('no')
print s.minInsertions('plkofzuofubstkjvmqpqnteukadjglraioqglvnhcjqwejdsmspzhvdsaopousfcbvmqtcndttciosvvkgvrfilkmnjkdeothndujhffchoalbtaltwwwtlatblaohcffhjudnhtoedkjnmklifrvgkvvsoicttdnctqmvbcfsuopoasdvhzpsmsdjewqjchnvlgqoiarlgjdakuetnqpqmvjktsbufouzfoklp')
