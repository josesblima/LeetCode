#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s, numRows):
        res = ['' for x in range(numRows)]
        while len(s) > 0:
            # Goes top to bottom vertically
            for x in range(numRows):
                if len(s) > 0:
                    res[x] += s[0]
                    s = s[1:]
                else:
                    print(''.join(res))
                    return ''.join(res)
            # Goes diagonally to the right
            for z in reversed(range(1,numRows - 1)):
                if len(s) > 0:
                    res[z] += s[0]
                    s = s[1:]
                else:
                    print(''.join(res))
                    return ''.join(res)
        print(''.join(res))
        return ''.join(res)
    convert(1, 'A', 1)    
# @lc code=end

