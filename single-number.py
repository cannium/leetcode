class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for a in A:
            ans = ans ^ a
        return ans
