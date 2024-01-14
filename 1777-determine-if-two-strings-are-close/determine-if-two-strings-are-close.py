#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
from collections import Counter
class Solution:
    def closeStrings(self, word1, word2) -> bool:
        wcounter1 = Counter(word1)
        print(wcounter1)
        wcounter2 = Counter(word2)
        print(wcounter2)
        print(wcounter1['a'])
        for letters in wcounter1:
            if wcounter2.get(letters) == None:
                return False
        for keys, values in wcounter1.items():
            for k, v in wcounter2.items():
                if values == v:
                    del wcounter2[k]
                    break
        if len(wcounter2) != 0:
            return False
        print(True)
        return True
    closeStrings(1, word1 = 'uau', word2 = 'ssx')
# @lc code=end

