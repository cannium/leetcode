class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        mapped = []
        status = None
        count = 0
        max1 = 0
        for i in range(len(A)):
            if status == 1 and count > max1:
                max1 = count
            if status is None:
                status = A[i]
                count = 1
                continue
            if status == A[i]:
                count += 1
            else:
                mapped.append((status, count))
                status = A[i]
                count = 1
        mapped.append((status, count))
        #print mapped
        ans = 0
        i, j = 0, 0
        this = 0
        remain = K
        while i < len(mapped):
            if i > 0:
                status_i, count_i = mapped[i-1]
                this -= count_i
                if status_i == 0:
                    remain += count_i
            while j < len(mapped):
                status, count = mapped[j]
                if status == 0:
                    if count <= remain:
                        this += count
                        remain -= count
                    else:
                        ans = max(ans, this+remain)
                        break
                else:
                    this += count
                j += 1
            if remain > 0 and i > 0:
                startstate, startcount = mapped[i-1]
                if startstate == 0:
                    ans = max(ans, this+min(startcount, remain))
            else:
                ans = max(ans, this)
            i += 1
        return ans
                
        
