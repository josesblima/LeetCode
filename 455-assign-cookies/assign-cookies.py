class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        list.sort(g)
        list.sort(s)
        kidlen = len(g)
        cookielen = len(s)
        kid = 0
        cookie = 0
        res = 0
        while True:
            if kid >= kidlen or cookie >= cookielen:
                return res
            if g[kid] <= s[cookie]:
                kid += 1
                cookie += 1
                res += 1
            else:
                cookie += 1
        return res            

