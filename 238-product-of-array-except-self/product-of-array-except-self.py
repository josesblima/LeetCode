#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums):
        left = [1]
        right = [1]
        prevnum = 1
        res = []
        # Multiplications starting on the left
        for number in nums:
            left.append(prevnum * number)
            prevnum = prevnum * number
        prevnum = 1
        # Multiplications starting on the right
        for number in reversed(nums):
            right.append(prevnum * number)
            prevnum = prevnum * number
        right.reverse()
        # Magic formula
        for index, number in enumerate(nums):
            res.append(left[index ] * right[index + 1])
        return res
    productExceptSelf(1, [1,2,3,4])
# @lc code=end

