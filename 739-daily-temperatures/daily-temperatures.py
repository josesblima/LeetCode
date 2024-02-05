class Solution:
    def dailyTemperatures(self, temperatures):
        stack = [temperatures[0]]
        stack_index = [0]
        for x in range(1, len(temperatures)):
            counter = 0
            while len(stack) >= 1 and temperatures[x] > stack[-1]:
                counter += 1
                popped_stack = stack_index.pop()
                temperatures[popped_stack] = x - popped_stack
                stack.pop()
            stack.append(temperatures[x])
            stack_index.append(x)
        for x in stack_index:
            temperatures[x] = 0
        return temperatures            


    dailyTemperatures(1, [55,38,53,81,61,93,97,32,43,78])
        
