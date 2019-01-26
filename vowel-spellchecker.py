aeiou = {
            'a':True,
            'e':True,
            'i':True,
            'o':True,
            'u':True,
}


def perm(listword):
    ans = []
    if listword[0] in aeiou:
        if len(listword) == 1:
            ans += ['a','e','i','o','u']
        else:
            perms = perm(listword[1:])
            for l in ['a','e','i','o','u']:
                for p in perms:
                    ans.append(l + p)
    else:
        if len(listword) == 1:
            ans.append(listword[0])
        else:
            perms = perm(listword[1:])
            for p in perms:
                ans.append(listword[0] + p)
    return ans

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        exact = {}
        capital = {}
        vowel = {}

        for w in wordlist:
            exact[w] = w
            
            lower = w.lower()
            if lower not in capital:
                capital[lower] = w
            
            perms = perm(list(lower))
            for p in perms:
                if p not in vowel:
                    vowel[p] = w
        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
                continue
            lower = q.lower()
            if lower in capital:
                ans.append(capital[lower])
                continue
            if lower in vowel:
                ans.append(vowel[lower])
                continue
            ans.append('')
        return ans