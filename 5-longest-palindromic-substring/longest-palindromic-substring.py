class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        def palicheck(left, right, s: str) -> str:
            global pali
            pali = ''
            if right < len(s):
                if s[left] != s[right]:
                    return pali
                else:
                    pali = s[left : right + 1]
            while left > 0 and right <= len(s) - 2 and s[left] == s[right]:
                    pali = s[left : right + 1]
                    left -= 1
                    right += 1
                    if s[left] != s[right]:
                        return pali
                    else:
                        pali = s[left : right + 1]
            return pali
        if len(s) == 0:
                res = ''
                return res
        if len(s) == 1:
                res = s
                return res
        for x in range(len(s) - 1):
            pali_even = palicheck(x, x+1, s)
            if len(pali_even) > len(res):
                res = pali
            pali_odd = palicheck(x, x+2, s)
            if len(pali_odd) > len(res):
                res = pali
        if len(s)>= 1 and res == '':
             res = s[0]
        
        
        print(res)
        return res
    longestPalindrome(1, "babad")