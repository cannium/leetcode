def d(n, memo):
    #print n, memo
    if n <= 1:
        return False
    if n in memo:
        return memo[n]
    for x in range(1, n):
        if n % x == 0 and d(n-x, memo) == False:
            memo[n] = True
            return True
    memo[n] = False
    return False

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        memo = {}
        return d(N, memo)
