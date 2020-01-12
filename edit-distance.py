def dp(memo, i, j, w1, w2):
    if i == len(w1) and j == len(w2):
        return 0
    if i == len(w1):
        return len(w2) - j
    if j == len(w2):
        return len(w1) - i
    if (i, j) in memo:
        return memo[(i,j)]
    if w1[i] == w2[j]:
        return dp(memo, i+1, j+1, w1, w2)
    ans = min(
        dp(memo, i+1, j, w1, w2),
        dp(memo, i, j+1, w1, w2),
        dp(memo, i+1, j+1, w1, w2),
    ) + 1
    memo[(i,j)] = ans
    return ans

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return dp(memo, i, j, word1, word2)