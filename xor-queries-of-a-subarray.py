class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        mem = [0] * len(arr)
        x = 0
        for i in range(0, len(arr)):
            if i == 0:
                mem[i] = arr[i]
                x = arr[i]
                continue
            x = arr[i] ^ x
            mem[i] = x
        #print mem
        ans = []
        for x, y in queries:
            if x == y:
                ans.append(arr[x])
                continue
            if x == 0:
                ans.append(mem[y])
                continue
            l = mem[x-1]
            r = mem[y]
            ans.append(l ^ r)
        #print ans 
        return ans

s = Solution()
s.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]])
s.xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]])
