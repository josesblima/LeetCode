#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        s1sort = ''.join(sorted(s1))
        for x in range(0, len(s2) - r):
            s2sort = ''.join(sorted(s2[l : r + 1]))
            if s1sort == s2sort:
                print('True')
                return True
            l += 1; r += 1
        print('False')
        return False

    checkInclusion(1, 'ba', 'oekjfrnabwe')

# @lc code=end
