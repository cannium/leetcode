def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def a(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans

class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        primeCount = 0
        for i in range(1, n+1):
            if isPrime(i):
                primeCount += 1
        return a(primeCount) * a(n-primeCount) % (10**9+7)
    

s = Solution()
print s.numPrimeArrangements(5)
print s.numPrimeArrangements(100)


