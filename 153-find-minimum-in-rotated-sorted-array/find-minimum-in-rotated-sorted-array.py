#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        # Check if it's already sorted
        if nums[right] >= nums[left] + (right - left):
            print(nums[left])
            return nums[left]
        while left < right - 1:
            midpoint = (left + right) // 2
            # Try go up
            if nums[midpoint] >= nums[left] + (midpoint - left):
                left = midpoint
            # Try go down
            elif nums[right] >= nums[midpoint] + (right - midpoint):
                right = midpoint
        print(nums[right])
        return nums[right]
# @lc code=end

    findMin(1,[11, 13, 15, 17])