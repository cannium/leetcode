class Solution:
    def countLetters(self, S: str) -> int:
        ans = 0
        letter = None
        count = 0
        for s in S:
            if letter is None:
                letter = s
                count = 1
                continue
            if letter == s:
                count += 1
                continue
            ans += (count+1) * count / 2
            letter = s
            count = 1
        ans += (count+1) * count / 2
        return int(ans)