class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans = 0
        already = [False] * (len(A)-1)
        for i in range(len(A[0])):
            ordered = True
            for j in range(1, len(A)):
                if already[j-1]:
                    continue
                if A[j][i] < A[j-1][i]:
                    ordered = False
                    break
            if not ordered:
                ans += 1
            else:
                for j in range(1, len(A)):
                    if A[j][i] > A[j-1][i]:
                        already[j-1] = True
        return ans
