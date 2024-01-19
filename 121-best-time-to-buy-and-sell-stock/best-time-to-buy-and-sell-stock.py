#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices):
        l = 0
        r = 1
        res = 0
        while r <= len(prices) - 1:
            # If left is higher or equalyou get no profit so move right
            if prices[l] >= prices[r]:
                l = r
                r += 1
                continue
            # If there's profit, update res if bigger than res
            if prices[l] < prices[r]:
                if res < prices[r] - prices[l]:
                    res = prices[r] - prices[l]
                r += 1
        print(res)
        return res
    maxProfit(1, [1,2,3,0,7])
# @lc code=end

