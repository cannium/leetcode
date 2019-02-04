class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        cur_lo = lower
        ans = []
        for n in nums:
            if n == cur_lo:
                cur_lo += 1
            else:
                ran = [cur_lo, n-1]
                cur_lo = n+1
                if ran[0] > ran[1]:
                    continue
                if ran[0] == ran[1]:
                    ans.append(str(ran[0]))
                else:
                    ans.append('%d->%d' % (ran[0], ran[1]))
        if cur_lo > upper:
            return ans
        if cur_lo == upper:
            ans.append(str(upper))
            return ans
        ans.append('%d->%d' % (cur_lo, upper))
        return ans
