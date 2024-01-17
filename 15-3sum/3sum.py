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
        # One for loop over the sorted list
        for count, x in enumerate(nums[:-1]):
            left = count + 1
            right = len(nums) - 1
            # This loop does the 2 pointers
            while True:
                # Checks if it's equal zero and stores result in hashset
                if x + nums[left] + nums[right] == 0 and right > left:
                    res.add(tuple([x, nums[left], nums[right]]))
                    right -= 1
                    continue
                # Checks if it's more than 0
                if x + nums[left] + nums[right] > 0 and left < right:
                    right -= 1
                    continue
                # Checks if it is less than 0
                if x + nums[left] + nums[right] < 0 and left < right:
                    left += 1
                    continue
                # If it didn't go into any of the if statements, it means
                # that search is over so it breaks and moves on to the next x
                break
        return res
    threeSum(1, [-1,0,1])
        
# @lc code=end

