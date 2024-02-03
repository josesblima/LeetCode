class Solution:
    def evalRPN(self, tokens) -> int:
        x = 0
        stack = []
        while x < len(tokens):
            try:
                stack.append(int(tokens[x]))
            except:
                if tokens[x] == '+':
                    new_num = stack[-2] + stack[-1]
                elif tokens[x] == '*':
                    new_num = stack[-2] * stack[-1]
                elif tokens[x] == '-':
                    new_num = stack[-2] - stack[-1]
                elif tokens[x] == '/':
                    new_num = stack[-2] / stack[-1]   
                stack[-2] = int(new_num)
                stack.pop() 
            x += 1
        return int(stack[0])