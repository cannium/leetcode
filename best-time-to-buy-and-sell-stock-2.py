class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        ## To complicated for this question...

        if not prices:
            return 0
        total = 0
        lastLow = 0
        lastHigh = 0
        lowPoints = 0
        highPoints = 0
        for i in range(1, len(prices) - 1):
            if prices[i] > prices[i - 1] and prices[i] >= prices[i+1]:
                total += (prices[i] - prices[lastLow])
                lastHigh = i
                highPoints += 1
            if prices[i] <= prices[i - 1] and prices[i] < prices[i+1]:
                lastLow = i
                lowPoints += 1

        if lastLow > lastHigh:
            total += (prices[len(prices)-1] - prices[lastLow])

        if lowPoints == 0 and highPoints == 0:
            if prices[len(prices)-1] > prices[0]:
                total += prices[len(prices)-1] - prices[0]

        return total

s = Solution()
print s.maxProfit([5,3,2,1,0,1,2,3,4,5,4])
print s.maxProfit([1,3,5,2,7,6,1])
print s.maxProfit([1,1,2,2,2,1,3])
print s.maxProfit([1,2,3,3,3,4,4])
print s.maxProfit([3,2,1])
