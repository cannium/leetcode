class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        profit = 0
        minStock = prices[0]
        maxStock = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > maxStock:
                maxStock = prices[i]
            if prices[i] < minStock:
                profit = max(profit, maxStock - minStock)
                minStock = prices[i]
                maxStock = prices[i]
        profit = max(profit, maxStock - minStock)
        return profit

s = Solution()
print s.maxProfit([5,3,2,1,0,1,2,3,4,5,4])
