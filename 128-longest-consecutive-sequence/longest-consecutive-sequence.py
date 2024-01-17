#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
import random
class Solution:
    def longestConsecutive(self, nums) -> int:
        nums_set = set(nums)
        res = 0
        left = None
        right = None
        # Function starts at a random spot and check
        # for consecutive numbers up and down whilst
        # removing reached numbers from the set
        def leftRightConsec(nums_set, left, right):
            if left in nums_set:
                nums_set.remove(left)
            if left - 1 in nums_set:
                if right + 1 in nums_set:
                    nums_set.remove(right + 1)
                    nums_set.remove(left - 1)
                    return leftRightConsec(nums_set, left - 1, right + 1)
                else:
                    nums_set.remove(left - 1)
                    return leftRightConsec(nums_set, left - 1, right)
            elif right + 1 in nums_set:
                nums_set.remove(right + 1)
                return leftRightConsec(nums_set, left, right + 1)
            return left, right
        if len(nums) == 0:
            return 0
        # This will call the function  at random
        # keys until it's empty
        while len(nums_set) > 0:
            random_number = nums_set.pop()
            print(random_number)
            left, right = leftRightConsec(nums_set, random_number, random_number)
            if right - left + 1 > res:
                res = right - left + 1
        return res
    longestConsecutive(1, [100,4,200,1,3,2])
# @lc code=end

