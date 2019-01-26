# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

from random import shuffle

def know(a, b, table):
    if a == b:
        return True
    if table[a][b] is None:
        ans = knows(a, b)
        table[a][b] = ans
        return ans
    return table[a][b]

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [[None for i in range(n)] for i in range(n)]
        possible = [i for i in range(n)]
        while len(possible) > 1:
            next_possible = []
            for i in range(len(possible)):
                if i == len(possible) - 1:
                    if not know(possible[i], possible[0], table) and know(possible[i-1], possible[i], table):
                        next_possible.append(possible[i])
                else:
                    if not know(possible[i], possible[i+1], table) and know(possible[i-1], possible[i], table):
                        next_possible.append(possible[i])
            possible = next_possible
            shuffle(possible)
        if len(possible) == 0:
            return -1
        c = possible[0]
        for i in range(n):
            if not know(i, c, table):
                return -1
            if i == c:
                continue
            if know(c, i, table):
                return -1
        return c
            
