#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            # Checks if current area is higher than res
            if min(height[l], height[r]) * (r - l) > res:
                res = min(height[l], height[r]) * (r - l)
            # Change one with exhausted potential
            if height[l] <  height[r]:
                l += 1  
                continue  
            if height[l] >=  height[r]:
                r -= 1
                continue
        return res
    maxArea(1, [1,3,2,5,25,24,5])
            
        
# @lc code=end

