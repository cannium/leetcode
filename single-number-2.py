class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        zero = ~0
        one = 0
        two = 0
        for a in A:
            new_zero = (two & a) | (zero & ~a)
            new_one = (zero & a) | (one & ~a)
            new_two = (one & a) | (two & ~a)
            zero = new_zero
            one = new_one
            two = new_two
            #print a, zero, one, two
        return one


s = Solution()
print s.singleNumber([1,1,1,2,3,2,2])
