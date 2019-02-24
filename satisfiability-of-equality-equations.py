def find(x, l):
    i = ord(x) - ord('a')
    while l[i] != -1:
        i = l[i]
    return i
    
def merge(a, b, l):
    ra = find(a, l)
    rb = find(b, l)
    if ra != rb:
        l[ra] = rb

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        l = [-1 for i in range(26)]
        for eq in equations:
            if eq[1] == '!':
                continue
            merge(eq[0],eq[3], l)
        for eq in equations:
            if eq[1] == '=':
                continue
            ra = find(eq[0], l)
            rb = find(eq[3], l)
            if ra == rb:
                return False
        return True
