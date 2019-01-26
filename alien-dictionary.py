def uniqs(words):
    uniq = {}
    for w in words:
        for c in w:
            uniq[c] = 1
    return uniq.keys()

def index(c):
    return ord(c) - ord('a')

def char(i):
    return chr(i+97)
    
def dfs(visitedInRecursion, now, d, visitedChar, stack):
    visitedChar[now] = 1
    for i in range(26):
        if now != i and d[now][i] == 1:
            if i in visitedInRecursion and visitedInRecursion[i] == 1:
                return True
            if visitedChar[i] == 1:
                continue
            visitedInRecursion[i] = 1
            circle = dfs(visitedInRecursion, i, d, visitedChar, stack)
            if circle:
                return True
            visitedInRecursion[i] = 0
    stack.append(now)
    return False

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) == 0:
            return ''

        uniq = uniqs(words)
        if len(words) == 1:
            return ''.join(uniq)
        
        d = [[0 for i in range(26)] for j in range(26)]
        for i in range(len(words) - 1):
            a = words[i]
            b = words[i+1]
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    d[index(a[j])][index(b[j])] = 1
                    break
        visitedChar = [0] * 26
        stack = []
        for c in uniq:
            ic = index(c)
            if visitedChar[ic] == 1:
                continue
            visitedInRecursion = {ic: 1}
            circle = dfs(visitedInRecursion, ic, d, visitedChar, stack)
            if circle:
                return ''

        return ''.join(char(x) for x in stack[::-1])
