def ordered(i, A):
    for j in range(1, len(A)):
        if A[j][i] < A[j-1][i]:
            return False
    return True

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans = 0
        for i in range(len(A[0])):
            if not ordered(i, A):
                ans += 1
        return ans
        
