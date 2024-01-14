# Really proud of this one but runtime error fml
# Everything works perfectly, just inefficient
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int):
        res = []
        alist = []
        blist = []
        for x in range(len(s)):
            if s[x: x + len(a)] == a:
                alist.append(x)
            if s[x: x + len(b)] == b:
                blist.append(x)
        for i in alist:
            for j in blist:
                if abs(j - i) <= k and j <= len(s) - len(b):
                    res.append(i)
                    break
        finres = list(dict.fromkeys(res))
        print(finres)
        return finres
    beautifulIndices(1,  s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15)