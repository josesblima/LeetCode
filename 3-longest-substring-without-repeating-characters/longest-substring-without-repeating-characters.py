class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strdic = {}
        res = 0
        char1 = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            # If letter repeats
            if s[i] in strdic: 
                #char1 be will 
                char1 = max(char1, strdic[s[i]] + 1)
                strdic[s[i]] = i
            else:
                strdic[s[i]] = i
            res = max(res, i - char1 + 1)
        print(strdic)
        print(res)
        return res
    lengthOfLongestSubstring(1, "tmmzuxt")