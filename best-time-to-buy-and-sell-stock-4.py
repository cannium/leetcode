def simplify(prices):
    useful = []
    for i, n in enumerate(prices):
        if i == 0 or i == len(prices) - 1:
            useful.append(n)
            continue
        if n >= prices[i-1] and n > prices[i+1]:
            useful.append(n)
            continue
        if n <= prices[i-1] and n < prices[i+1]:
            useful.append(n)
            continue
    return useful

def quickSolve(prices):
    ans = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            ans += prices[i] - prices[i-1]
    return ans

class Solution:
    def maxProfit(self, k, prices):
        if len(prices) < 2:
            return 0
        useful = simplify(prices)
        useful = simplify(useful)
        print(useful)
        if k >= len(useful) / 2:
            return quickSolve(useful)
        hold = [[0 for j in range(0, len(useful))] for i in range(0, k+1)]
        unhold = [[0 for j in range(0, len(useful))] for i in range(0, k+1)]
        hold[0][0] = -useful[0]
        for i in range(1, k+1):
            hold[i][0] = -useful[0]
        for j in range(1, len(useful)):
            hold[0][j] = max(hold[0][j-1], -useful[j])
        for i in range(1, k+1):
            for j in range(1, len(useful)):
                hold[i][j] = max(hold[i][j-1], unhold[i][j-1] - useful[j])
                unhold[i][j] = max(unhold[i][j-1], hold[i-1][j-1] + useful[j])
        return max(hold[k][len(useful)-1], unhold[k][len(useful)-1])

import sys
sys.setrecursionlimit(1000000000)

s = Solution()
print(s.maxProfit(2, [2,4,1]))
print(s.maxProfit(2, [3,2,6,5,0,3]))
print(s.maxProfit(2, [3,3,5,0,0,3,1,4]))
print(s.maxProfit(2, [1,2,4,2,5,7,2,4,9,0]))
print(s.maxProfit(1, [6,1,6,4,3,0,2]))
print(s.maxProfit(2, [0,5,5,6,2,1,1,3]))