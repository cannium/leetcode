def reverse(ls, l, r):
    while l < r:
        ls[l], ls[r] = ls[r], ls[l]
        l += 1
        r -= 1

class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        reverse(str, 0, len(str)-1)
        i = None
        for j in range(len(str)):
            if str[j] == ' ':
                if i is None:
                    continue
                else:
                    reverse(str, i, j-1)
                    i = None
            else:
                if i is None:
                    i = j
        if i is not None:
            reverse(str, i, len(str)-1)
