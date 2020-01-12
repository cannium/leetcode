keys = {
    'A': (0,0),
    'B': (0,1),
    'C': (0,2),
    'D': (0,3),
    'E': (0,4),
    'F': (0,5),
    'G': (1,0),
    'H': (1,1),
    'I': (1,2),
    'J': (1,3),
    'K': (1,4),
    'L': (1,5),
    'M': (2,0),
    'N': (2,1),
    'O': (2,2),
    'P': (2,3),
    'Q': (2,4),
    'R': (2,5),
    'S': (3,0),
    'T': (3,1),
    'U': (3,2),
    'V': (3,3),
    'W': (3,4),
    'X': (3,5),
    'Y': (4,0),
    'Z': (4,1)
}

def dist(now, next):
    if now is None:
        return 0
    x1, y1 = keys[now]
    x2, y2 = keys[next]
    return abs(x1-x2) + abs(y1-y2)

def dp(memo, i, f1, f2, word):
    if i >= len(word):
        return 0
    if (i, f1, f2) in memo:
        return memo[(i, f1, f2)]
    nextWord = word[i]
    ans = min(
        dp(memo, i+1, nextWord, f2, word) + dist(f1, nextWord),
        dp(memo, i+1, f1, nextWord, word) + dist(f2, nextWord)
    )
    memo[(i, f1, f2)] = ans
    return ans

class Solution:
    def minimumDistance(self, word: str) -> int:
        memo = {}
        return dp(memo, 0, None, None, word)