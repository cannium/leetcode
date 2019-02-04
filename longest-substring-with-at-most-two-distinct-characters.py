class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        change = [0]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                change.append(i)
        change.append(len(s))
        if len(change) <= 3:
            return len(s)
        ans = change[2]
        cur_size = change[2]
        #print change
        for i in range(2, len(change)-1):
            if change[i] == len(s) or s[change[i]] == s[change[i-2]]:
                cur_size += (change[i+1] - change[i])
            else:
                cur_size = change[i+1] - change[i-1]
            if cur_size > ans:
                ans = cur_size
        return ans
