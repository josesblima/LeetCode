#
# @lc app=leetcode id=2180 lang=python3
#
# [2180] Count Integers With Even Digit Sum
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for x in range(1, num + 1):
            digits = []
            curx = x
            cursum = 0
            while True:
                if curx <= 9:
                    digits.append(curx)
                    cursum = sum(digits)
                    break
                    
                digits.append(curx % 10)
                curx-= (curx % 10)
                curx /= 10
            if cursum % 2 == 0:
                res += 1
        print(res)
        return res
    countEven(1, 345)
# @lc code=end

