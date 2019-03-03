from collections import defaultdict

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        memo = defaultdict(lambda: 0)
        for i in range(len(prices)-1, -1, -1):
            buy = prices[i]
            jbuy, jnone, buy_price
            for j in range(len(prices)-1, i-1, -1):
                memo[(j, buy)] = max(memo[(j, buy)], memo[(j+1, buy)], memo[(j+2, None)]+prices[j]-buy)
                memo[(j, None)] = max(memo[(j, None)], memo[(j+1, None)], memo[(j+1, prices[j])])

        return memo[(0, None)]
        
