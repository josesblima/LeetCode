#
# @lc app=leetcode id=2455 lang=python3
#
# [2455] Average Value of Even Numbers That Are Divisible by Three
#

# @lc code=start
class Solution:
    def averageValue(self, nums) -> int:
        res = []
        for x in nums:
            if x % 2 == 0 and x % 3 == 0:
                res.append(x)
        if len(res) > 0:
            print(res)
            finres = sum(res) // len(res)
            print(finres)
            return finres
        return 0
    averageValue(1, [1,3,6,10,12,15])
# @lc code=end

