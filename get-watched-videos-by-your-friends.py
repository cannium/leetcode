def cmp(x, y):
    if x[1] == y[1]:
        if x[0] < y[0]:
            return -1
        elif x[0] == y[0]:
            return 0
        else:
            return 1
    elif x[1] < y[1]:
        return -1
    else:
        return 1

class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        visited = {id: True}
        fs = [id]
        while level > 0:
            level -= 1
            newFs = {}
            for f in fs:
                for ff in friends[f]:
                    if ff in visited:
                        continue
                    visited[ff] = True
                    newFs[ff] = 1
            fs = newFs.keys()
        vs = {}
        for f in fs:
            for v in watchedVideos[f]:
                if v in vs:
                    vs[v] += 1
                else:
                    vs[v] = 1
        #print vs
        ans = []
        for k, v in sorted(vs.items(), cmp=cmp):
            ans.append(k)
        return ans

s = Solution()
print s.watchedVideosByFriends([["A","B"],["C"],["B","C"],["D"]], [[1,2],[0,3],[0,3],[1,2]], 0, 1)