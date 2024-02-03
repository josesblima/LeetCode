class Solution:
    def evalRPN(self, tokens) -> int:
        x = 0
        intcheck = None
        while x < len(tokens):
            try:
                tokens[x] = int(tokens[x])
                x += 1
            except:
                if tokens[x] == '+':
                    new_num = tokens[x-2] + tokens[x-1]

                if tokens[x] == '*':
                    new_num = tokens[x-2] * tokens[x-1]
                if tokens[x] == '-':
                    new_num = tokens[x-2] - tokens[x-1]

                if tokens[x] == '/':
                    new_num = int(tokens[x-2] / tokens[x-1])   
                tokens[x-2] = new_num
                tokens.pop(x)
                tokens.pop(x - 1)
                x -= 1
        return tokens[0]


    evalRPN(1, ["5", "2", "/"])