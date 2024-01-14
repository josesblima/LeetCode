class Solution:
    def isValid(self, s: str) -> bool:
        prevx = ''
        res = None
        for _ in range(len(s) // 2):
            for x in range(len(s)):
                if x != len(s) - 1:
                    if s[x] == '(' and s[x + 1] == ')':
                        s = s[:x] + s[x + 2:]
                        break
                    if s[x] == '[' and s[x + 1] == ']':
                        s = s[:x] + s[x + 2:]
                        break
                    if s[x] == '{' and s[x + 1] == '}':
                        s = s[:x] + s[x + 2:]
                        break
        if len(s) > 0:
            res = False
        else:
            res = True
        print(res)
        return res
    isValid(1, '{([}])')