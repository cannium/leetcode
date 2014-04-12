class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        left = [a - b for a, b in zip(gas, cost)]
        if sum(left) < 0:
            return -1
        
        tank = 0
        start = 0
        for i in range(len(left)):
            if tank + left[i] < 0:
                tank = 0
                start = i + 1
            else:
                tank += left[i]

        return start


s = Solution()
print s.canCompleteCircuit([4,3,0,1], [3.5,2.4,1,1.1])
