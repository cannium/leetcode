class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(0, len(s)):
            if i == 0:
                if s[i] == '0':
                    return 0
                dp[i] = 1
                continue
            if s[i] == '0':
                if s[i-1] != '1' and s[i-1] != '2':
                    return 0
                if i >= 2:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 1
                continue
            if s[i-1] == '0':
                dp[i] = dp[i-1]
                continue
            if int(s[i-1:i+1]) <= 26:
                if i >= 2:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1] + 1
                continue
            dp[i] = dp[i-1]
        print(dp)
        return dp[len(s)-1]
