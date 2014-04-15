class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        # A[n] is the largest profit with one transaction
        # for 0...n
        A = [0]
        lowest = prices[0]
        highest = prices[0]
        # B[n] is the largest profit with two transactions at most
        B = [0]
        for i in range(1, len(prices)):
            if prices[i] >= highest:
                highest = prices[i]
                A.append(highest - lowest)
                        
                best = 0
                for j in range(0, i):
                    if best < A[j] + prices[i] - prices[j+1]:
                        best = A[j] + prices[i] - prices[j+1]
                B.append(max(A[i], best, B[i-1]))

            elif prices[i] <= lowest:
                lowest = prices[i]
                A.append(A[i-1])
                B.append(B[i-1])
            else:
                A.append(max(A[i-1], prices[i] - lowest))
                
                best = 0
                for j in range(0, i):
                    if best < A[j] + prices[i] - prices[j+1]:
                        best = A[j] + prices[i] - prices[j+1]
                B.append(max(A[i], best, B[i-1]))
        print A, B
        return B[-1]
    # for better answer (O(n) solution), see
    # http://oj.leetcode.com/discuss/1381/any-solutions-better-than-o-n-2

s = Solution()
print s.maxProfit([1,2,4,2,5,7,2,4,9,0])
print s.maxProfit([4,1,2])
print s.maxProfit([2,1,2,0,1])
print s.maxProfit([6,1,3,2,4,7])
