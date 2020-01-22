from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [2*n] * (n+1)
        dp[0] = 0
        for i, x in enumerate(ranges):
            for j in range(max(0, i-x), min(n, i+x)+1):
                dp[j] = min(dp[j], dp[max(0, i-x)]+1)
        if dp[n] != 2 * n:
            return dp[n]
        return -1

                



        