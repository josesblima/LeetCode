#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0,1]
        for x in range(0, n):
            res.append(res[-2] + res[-1])
            print(res)
        return res[-1]
    climbStairs(1, 5)
# @lc code=end

