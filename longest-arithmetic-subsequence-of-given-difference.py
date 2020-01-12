class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = [1] * len(arr)
        last = {}
        for i in range(len(arr)):
            x = arr[i]
            need = x - difference
            if need not in last:
                last[x] = i
                continue
            last_i = last[need]
            dp[i] = max(dp[i], dp[last_i] + 1)
            last[x] = i
        return max(dp)