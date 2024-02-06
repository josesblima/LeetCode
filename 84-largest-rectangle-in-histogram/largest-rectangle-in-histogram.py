class Solution:
    def largestRectangleArea(self, heights):
                    # Height, total area, index
        stack = [   [heights[0], heights[0], 0]   ]
        res = heights[0]
        multiplier = 1
        for x in range(1, len(heights)):
            if x + 1 < len(heights)and heights[x - 1] == heights[x] and heights[x] == heights[x + 1]:
                multiplier += 1
                continue
            # If number increased
            if len(stack) >= 1 and heights[x] > stack[-1][0]:
                for z in range(len(stack)):
                    # Update stack values
                    stack[z][1] += stack[z][0]
                    if stack[z][1] > res:
                        res = stack[z][1]
                # Append new value
                stack.append([heights[x],heights[x],x])
                if stack[-1][1] > res:
                        res = stack[-1][1]
                continue
            # If number decreased
            if len(stack) >= 1 and heights[x] < stack[-1][0]:
                popcount = 0
                # Pop all the last elems of stack until the last elem stops being higher than
                # current elem and keep track of how many were popped to multiply them by new value
                while len(stack) >= 1 and heights[x] < stack[-1][0]:
                    lastpop = stack.pop()
                    popcount += 1
                if len(stack) == 0:
                    stack.append([heights[x],  (x + 1 - lastpop[2]) * heights[x],lastpop[2]])
                    if stack[-1][1] > res:
                        res = stack[-1][1]
                    continue
                if heights[x] >= stack[-1][0]:
                    # Append and multiply total area by popcount
                    stack.append([heights[x], (x + 1 - lastpop[2]) * heights[x],lastpop[2]])
                    if stack[-1][1] > res:
                        res = stack[-1][1]
                    for z in range(0,len(stack) - 1):
                        # Update stack values
                        stack[z][1] += stack[z][0]
                        if stack[z][1] > res:
                            res = stack[z][1]
                    continue
            for z in range(len(stack)):
                # Update stack values
                    stack[z][1] += stack[z][0] * multiplier
                    if stack[z][1] > res:
                        res = stack[z][1]
            multiplier = 1
        return res
    largestRectangleArea(1, 
                         [7,4,5,9,0,1,1,8,3,1,6,8,8,8,8,0,7,7,8])