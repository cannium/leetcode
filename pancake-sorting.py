
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        order = sorted(A)
        location = {}
        for i in xrange(len(A)):
            location[A[i]] = i
        ans = []
        for i in range(len(order)-1, -1, -1):
            n = order[i]
            k = location[n]
            if k == i:
                continue
            a = 0
            b = k
            while a < b:
                A[a], A[b] = A[b], A[a]
                location[A[a]] = a
                location[A[b]] = b
                a += 1
                b -= 1
            a = 0
            b = i
            while a < b:
                A[a], A[b] = A[b], A[a]
                location[A[a]] = a
                location[A[b]] = b
                a += 1
                b -= 1
            ans += [k+1, i+1]
        return ans
