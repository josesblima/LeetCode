class Solution:
    def firstPalindrome(self, words) -> str:
        for z in words:
            l = 0; r = len(z) - 1
            pali = True
            while l < len(z) // 2:
                if z[l] != z[r]:
                    pali = False
                    break
                l += 1; r -= 1
            if pali == True:
                return z
        return ""