def find_i(arr, l, r, target):
    while l < r:
        mid = l + (r-l)/2
        if arr[mid][2] < target:
            l = mid + 1
        else:
            r = mid
    return l

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.d:
            self.d[key] = [(key, value, timestamp)]
            return
        i = find_i(self.d[key], 0, len(self.d[key]), timestamp)
        if i >= len(self.d[key]):
            self.d[key].append((key,value,timestamp))
        else:
            self.d[key].insert(i, (key,value,timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.d:
            return ''
        i = find_i(self.d[key], 0, len(self.d[key]), timestamp)
        if i >= len(self.d[key]):
            return self.d[key][len(self.d[key])-1][1]
        else:
            if self.d[key][i][2] == timestamp:
                return self.d[key][i][1]
            elif i - 1 >= 0:
                return self.d[key][i-1][1]
            else:
                return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
