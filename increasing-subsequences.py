class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        memo = {}
        def find(n):
            if n in memo:
                return memo[n]
            ans = []
            for i in range(n, len(nums)):
                ans.append([nums[i]])
                for j in range(i+1, len(nums)):
                    if nums[j] >= nums[i]:
                        j_ans = find(j)
                        for aj in j_ans:
                            if aj[0] >= nums[i]:
                                ans.append([nums[i]] + aj)
            ans = sorted(ans)
            an = []
            for i in range(len(ans)):
                if i == 0:
                    an.append(ans[i])
                    continue
                if ans[i] != ans[i-1]:
                    an.append(ans[i])
            memo[n] = an
            return an
        a0 = find(0)
        ret = []
        for a in a0:
            if len(a) >= 2:
                ret.append(a)
        return ret