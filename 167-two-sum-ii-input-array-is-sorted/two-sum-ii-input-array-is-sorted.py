#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers, target: int):
        left = 0
        right = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            # Checks if sum is greater than target
            # and decreases right or increases left
            if numbers[left] + numbers[right] > target and right > 0:
                right -= 1
                continue
            if numbers[left] + numbers[right] < target and left < len(numbers) - 1:
                left += 1
                continue
        return [left + 1, right + 1]
    twoSum(1, [3,24,50,79,88,150,345], 200)
        
# @lc code=end

