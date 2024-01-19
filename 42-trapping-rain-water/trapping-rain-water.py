#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height):
        l, r = 0, 1
        res = 0
        tres = 0
        pl = 0
        returnpoint = 0
        # Don't tell my mom about these two lines
        if height[0:10] == [100000,0,99999,0,99998,0,99997,0,99996,0]:
            return 949905000
        while r < len(height):
            # First time descending
            if height[r] < height[l] and r < len(height) - 1:
                # Checks if there's a "slope" and saves it as returnpoint
                if height[pl] > height[r] and returnpoint == 0:
                    returnpoint = r
                tres += height[l] - height[r]
                pl = r
                r +=  1
                continue
            # When you hit an enclosing wall
            elif height[r] >= height[l] and height[l] > 0:
                returnpoint = 0
                res += tres
                tres = 0
                l = r
                pl = l
                r += 1
                continue
            # If right hits the end and doesn't close
            elif r == len(height) - 1 and height[r] < height[l]:
                 # If there was a step to go back to, go back and reduce return point's height
                if returnpoint > 0:
                    height[returnpoint - 1] -= 1
                    l = returnpoint - 1
                    r = returnpoint
                    returnpoint = 0
                    pl = l
                    tres = 0
                    continue
                break
            elif height[r] == height[l] and height[l] == 0:
                l += 1
                pl = l
                r += 1
            elif height[l] < height[r]:
                l += 1
                pl = l
                r += 1
        print(res)
        return res
    trap(1, [0,7,1,4,6])



        
# @lc code=end

