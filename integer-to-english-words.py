n = {
    1:'One',
    2:'Two',
    3:'Three',
    4:'Four',
    5:'Five',
    6:'Six',
    7:'Seven',
    8:'Eight',
    9:'Nine',
    10:'Ten',
    11:'Eleven',
    12:'Twelve',
    13:'Thirteen',
    14:'Fourteen',
    15:'Fifteen',
    16:'Sixteen',
    17:'Seventeen',
    18:'Eighteen',
    19:'Nineteen',
    20:'Twenty',
}

ty = {
    2:'Twenty',
    3:'Thirty',
    4:'Forty',
    5:'Fifty',
    6:'Sixty',
    7:'Seventy',
    8:'Eighty',
    9:'Ninety',
}

def speak(num):
    ans = []
    if num / 10**9 >= 1:
        ans += speak(num/10**9)
        ans.append('Billion')
        num = num % 10**9
    if num / 10**6 >= 1:
        ans += speak(num/10**6)
        ans.append('Million')
        num = num % 10**6
    if num / 10**3 >= 1:
        ans += speak(num/10**3)
        ans.append('Thousand')
        num = num % 10**3
    if num / 10**2 >= 1:
        ans += speak(num/10**2)
        ans.append('Hundred')
        num = num % 10**2
    if num > 20:
        ans.append(ty[num/10])
        if num % 10 != 0:
            ans.append(n[num%10])
    elif num == 0:
        if len(ans) == 0:
            ans.append('Zero')
    else:
        ans.append(n[num])
    return ans

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = speak(num)
        return ' '.join(ans)
