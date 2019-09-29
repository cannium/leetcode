def remove(s, k):
    ss = list(s)
    last = None
    lasti = None
    count = 0
    for i in range(len(s)):
        if last is None:
            last = s[i]
            lasti = i
            count = 1
            continue
        if s[i] == last:
            count += 1
            if count >= k:
                ss[lasti:i+1] = [''] * (i+1-lasti)
                if lasti-1 >= 0:
                    lasti = lasti - 1
                    last = ss[lasti]
                    count = 1
                else:
                    last = None
                    count = 0
        else:
            last = s[i]
            lasti = i
            count = 1
    return ''.join(ss)
        

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        last = s
        while True:
            ss = remove(last, k)
            if ss == last:
                return ss
            last = ss


s = Solution()
print s.removeDuplicates("nnwssswwnvbnnnbbqhhbbbhmmmlllm", 3)