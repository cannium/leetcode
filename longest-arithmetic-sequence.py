def found(x, memo, now):
    if x not in memo:
        return -1
    for i in memo[x]:
        if i > now:
            return i
    return -1

class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        memo = {}
        for i in range(len(A)):
            a = A[i]
            if a in memo:
                memo[a].append(i)
            else:
                memo[a] = [i]
        ans = 2
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                d = A[j] - A[i]
                now = j
                count = 2
                while True:
                    n = found(A[now] + d, memo, now)
                    if n == -1:
                        break
                    now = n
                    count += 1
                ans = max(ans, count)
        return ans
