#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        revs = s[::-1]
        if s == revs:
            return True
        return False
    isPalindrome(1, "A man, a plan, a canal: Panama")
# @lc code=end

