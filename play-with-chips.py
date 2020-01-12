class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        odd = 0
        even = 0
        for x in chips:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)