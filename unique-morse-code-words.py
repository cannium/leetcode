l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        m = {}
        for i in range(26):
            m[chr(ord('a')+i)] = l[i]
        trans = {}
        for w in words:
            tran = ''
            for c in w:
                tran += m[c]
            trans[tran] = 1
        return len(trans.keys())
