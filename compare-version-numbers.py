class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) < len(v2):
            v1 += [0] * (len(v2) - len(v1))
        else:
            v2 += [0] * (len(v1) - len(v2))
        for i in range(len(v1)):
            n1 = int(v1[i])
            n2 = int(v2[i])
            if n1 == n2:
                continue
            if n1 > n2:
                return 1
            else:
                return -1
        return 0
