"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def __init__(self):
        self.bf = []
        self.old_size = 0
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        nn = 0
        while nn < n:
            if self.old_size > 0:
                if self.old_size >= n:
                    buf[nn:n] = self.bf[:n-nn]
                    self.bf = self.bf[n:]
                    self.old_size = self.old_size - n
                    return n
                else:
                    buf[nn:nn+self.old_size] = self.bf
                    nn += self.old_size
                    self.bf = []
                    self.old_size = 0

            bf = [' '] * 4
            n4 = read4(bf)
            if nn + n4 > n:
                buf[nn:n] = bf[:n-nn]
                self.bf = bf[n-nn:]
                self.old_size = nn+n4-n
                return n
            buf[nn:nn+n4] = bf
            nn += n4
            if n4 < 4:
                return nn
        return nn
