class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return 1
        trusts = {}
        trusted = {}
        for a, b in trust:
            if a in trusts:
                trusts[a] += 1
            else:
                trusts[a] = 1
            if b in trusted:
                trusted[b] += 1
            else:
                trusted[b] = 1
        for i in range(1, N+1):
            if i in trusted:
                if trusted[i] == N-1 and i not in trusts:
                    return i
        return -1
