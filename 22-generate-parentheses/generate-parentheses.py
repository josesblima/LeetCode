#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int):
        res = []
        lb = 0
        rb = 0
        s = ''
        n *= 2
        def parenthetitsMachine(s, n, lb, rb):
            if len(s) >= n: 
                res.append(s)
                return
            # Check if can '('
            if (lb < n/2 and n - len(s) >= n/2 - rb) or lb == rb:
                parenthetitsMachine(s + '(', n, lb + 1, rb)
            # Check if can ')'
            if lb > rb:
                parenthetitsMachine(s + ')', n, lb, rb + 1)
        parenthetitsMachine(s, n, lb, rb)
        print(res)
        return res
    generateParenthesis(1, 4)

# @lc code=end