class Solution:
    def largestRectangleArea(self, heights):
                    # Height, total area, index
        stack = [   [heights[0], heights[0], 0]   ]
        res = heights[0]
        multiplier = 1
        for x in range(1, len(heights)):
            # Little hack for the alg to become more efficient when it faces consecutive equal numbers,
            # instead of updating the stack, it just increases a multiplier that will be applied as soon
            # as the next number is different (very bottom of the function)
            if x + 1 < len(heights)and heights[x - 1] == heights[x] and heights[x] == heights[x + 1]:
                multiplier += 1
                continue
            # If number increased
            if len(stack) >= 1 and heights[x] > stack[-1][0]:
                # for z in range(len(stack)):
                #     # Update stack values
                #     stack[z][1] += stack[z][0]
                #     if stack[z][1] > res:
                #         res = stack[z][1]
                # Append new value
                stack.append([heights[x],heights[x],x])
                if stack[-1][1] > res:
                        res = stack[-1][1]
                continue
            # If number decreased
            if len(stack) >= 1 and heights[x] < stack[-1][0]:
                # Pop all the last elems of stack until the last elem stops being higher than
                # current elem and keep track of the last popped elem to know how many times
                # to add the value of the new item
                while len(stack) >= 1 and heights[x] < stack[-1][0]:
                    lastpop = stack.pop()
                    #update result if the area of lastpop is higher
                    if res < lastpop[1] * (x - lastpop[2]):
                        res = lastpop[1] * (x - lastpop[2])
                # If stack is empty just append
                if len(stack) == 0:
                    stack.append([heights[x], heights[x],lastpop[2]])
                    if stack[-1][1] > res:
                        res = stack[-1][1]
                    continue
                # I stack is not empty, append and update the other elems
                if heights[x] >= stack[-1][0]:
                    # Append and multiply total area by popcount
                    stack.append([heights[x], heights[x],lastpop[2]])
                    if stack[-1][1] > res:
                        res = stack[-1][1]
                    continue
                    # for z in range(0,len(stack) - 1):
                    #     # Update stack values
                    #     stack[z][1] += stack[z][0]
                    #     if stack[z][1] > res:
                    #         res = tack[z][1]
                    # continue
            # If value is equal to last elem of stack 
            if len(stack) >= 1 and heights[x] == stack[-1][0]:
                continue

            # This is where it goes after a streak of repetitions
            for z in range(len(stack)):
                # Update stack values
                    stack[z][1] += stack[z][0] * multiplier
                    if stack[z][1] > res:
                        res = stack[z][1]
            multiplier = 1
        popcounter = 0
        while len(stack) > 0:
            popcounter += 1
            lastpop = stack.pop()
            #update result if the area of lastpop is higher
            if res < lastpop[1] * (len(heights) - lastpop[2]):
                res = lastpop[1] * (len(heights) - lastpop[2])
        return res
    largestRectangleArea(1, [1,1])
    