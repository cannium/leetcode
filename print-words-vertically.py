from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        longest = 0
        for w in words:
            if len(w) > longest:
                longest = len(w)
        ans = []
        for i in range(0, longest):
            vertical = []
            for w in words:
                if i >= len(w):
                    vertical.append(' ')
                else:
                    vertical.append(w[i])
            vw = ''.join(vertical)
            vw = vw.rstrip()
            ans.append(vw)
        return ans

        