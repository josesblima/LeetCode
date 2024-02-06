class Solution:
    def largestRectangleArea(self, heights):
                    # Height, total area, index
        stack = [   [heights[0], heights[0], 0]   ]
        res = heights[0]
        for x in range(1, len(heights)):
            # If number increased
            if len(stack) >= 1 and heights[x] > stack[-1][0]:
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
        popcounter = 0
        while len(stack) > 0:
            popcounter += 1
            lastpop = stack.pop()
            #update result if the area of lastpop is higher
            if res < lastpop[1] * (len(heights) - lastpop[2]):
                res = lastpop[1] * (len(heights) - lastpop[2])
        return res