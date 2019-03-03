from collections import defaultdict

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col = defaultdict(lambda: False)
        diag1 = defaultdict(lambda: False)
        diag2 = defaultdict(lambda: False)
        total = [0]
        def dig(row):
            if row >= n:
                total[0] += 1
                return
            for i in range(n):
                if col[i] or diag1[row-i] or diag2[row+i]:
                    continue
                col[i], diag1[row-i], diag2[row+i] = True, True, True
                dig(row+1)
                col[i], diag1[row-i], diag2[row+i] = False, False, False
        dig(0)
        return total[0]

s = Solution()
print s.totalNQueens(4)
print s.totalNQueens(8)