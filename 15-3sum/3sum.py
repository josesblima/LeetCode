#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = set()
        for count, x in enumerate(nums[:-1]):
            left = count + 1
            right = len(nums) - 1
            while True:
                if x + nums[left] + nums[right] == 0 and right > left:
                    res.add(tuple([x, nums[left], nums[right]]))
                    right -= 1
                    continue
                if x + nums[left] + nums[right] > 0 and left < right:
                    right -= 1
                    continue
                if x + nums[left] + nums[right] < 0 and left < right:
                    left += 1
                    continue
                break
        print(res)
        return res
    threeSum(1, [-1,0,1])
        
# @lc code=end

