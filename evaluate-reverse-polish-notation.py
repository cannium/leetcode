class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t in ['+','-','*','/']:
                y = stack.pop()
                x = stack.pop()
                ans = 0 
                if t == '+':
                    ans = x + y
                elif t == '-':
                    ans = x - y
                elif t == '*':
                    ans = x * y
                else:
                    if x/y < 0:
                        ans = -(-x/y)
                    else:
                        ans = x/y
                stack.append(ans)
            else:
                stack.append(int(t))
        return stack[0]
