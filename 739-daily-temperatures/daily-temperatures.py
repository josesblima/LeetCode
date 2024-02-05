class Solution:
    def dailyTemperatures(self, temperatures):
        # We keep track of values in stack until the temperature rises
        stack = [temperatures[0]]
        # Keep track of the index of each value in the stack
        stack_index = [0]
        for x in range(1, len(temperatures)):
            # Every time the temperature rises, we remove from the end of the stack
            while len(stack) >= 1 and temperatures[x] > stack[-1]:
                popped_stack = stack_index.pop()
                temperatures[popped_stack] = x - popped_stack
                stack.pop()
            stack.append(temperatures[x])
            stack_index.append(x)
        # At the end, there might still be items in the stack, which means
        # temperature won't ever rise withing the given days, so we change them to 0
        for x in stack_index:
            temperatures[x] = 0
        return temperatures