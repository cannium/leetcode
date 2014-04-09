class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        while len(tokens) > 1:
            l = len(tokens)
            for i in range(l):
                if str(tokens[i]) in '+-*/':
                    ans = self.compute(tokens[i], tokens[i-1], tokens[i-2])
                    tokens.pop(i)
                    tokens.pop(i-1)
                    tokens.pop(i-2)
                    tokens.insert(i-2, ans)
                    break
        return int(tokens[0])

    def compute(self, op, n1, n2):
        n1 = int(n1)
        n2 = int(n2)
        if op == '+':
            return n1 + n2
        elif op  == '-':
            return n2 - n1
        elif op  == '*':
            return n1 * n2
        elif op == '/':
            return int(1.0 * n2 / n1)

