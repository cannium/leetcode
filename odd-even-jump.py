def bs(arr, l, r, target):
    while l < r:
        mid = l + (r-l)/2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #print A
        d = {}
        for i in range(len(A)):
            n = A[i]
            if n in d:
                d[n].append(i)
            else:
                d[n] = [i]
        ns = sorted(d.keys())
        #print d
        nextBig = [-1] * len(A)
        nextSmall = [-1] * len(A)
        for i in range(len(A)):
            N = A[i]
            ni = bs(ns, 0, len(ns), N)
            #print 'ni', ni, 'ns', ns, 'N', N
            if len(d[N]) > 1:
                dni = bs(d[N], 0, len(d[N]), i)
                if dni + 1 < len(d[N]):
                    nextSmall[i] = d[N][dni+1]
                    nextBig[i] = d[N][dni+1]
                    continue
            ii = ni + 1
            while ii < len(ns):
                n = ns[ii]
                #print 'N', N, 'n', n, 'ns', ns, 'ii', ii
                if len(d[n]) >= 1:
                    dni = bs(d[n], 0, len(d[n]), i)
                    #print 'd[n]', d[n], 'dni', dni, 'i',i
                    if dni < len(d[n]) and d[n][dni] > i:
                        nextBig[i] = d[n][dni]
                        break
                ii += 1
            ii = ni - 1
            while ii >= 0:
                n = ns[ii]
                if len(d[n]) >= 1:
                    dni = bs(d[n], 0, len(d[n]), i)
                    #print dni, ii, d[n], i, ni, ns
                    if dni < len(d[n]) and d[n][dni] > i:
                        nextSmall[i] = d[n][dni]
                        break
                ii -= 1
        #print nextBig
        #print nextSmall
        seen = [0] * len(A)
        oddmemo = {}
        evenmemo = {}
        ans = 0
        for i in range(len(A)):
            step = 1
            if i in oddmemo:
                if oddmemo[i]:
                    ans += 1
                continue
            j = i
            flag = False
            memo = [j]
            while True:
                if j == -1:
                    break
                if j == len(A) - 1:
                    flag = True
                    break
                if step % 2 == 1:
                    if j in oddmemo and oddmemo[j]:
                        flag = True
                        break
                else:
                    if j in evenmemo and evenmemo[j]:
                        flag = True
                        break
                
                if step % 2 == 1:
                    j = nextBig[j]
                else:
                    j = nextSmall[j]
                memo.append(j)
                step += 1
            if flag:
                ans += 1
            while step > 0:
                if step % 2 == 1:
                    oddmemo[i] = flag
                else:
                    evenmemo[i] = flag
                step -= 1
        #print oddmemo
        #print evenmemo
        return ans
                    
            
            
s = Solution()
print s.oddEvenJumps([10,13,12,14,15])
print s.oddEvenJumps([2,3,1,1,4])
print s.oddEvenJumps([5,1,3,4,2])
print s.oddEvenJumps([61,91,96])