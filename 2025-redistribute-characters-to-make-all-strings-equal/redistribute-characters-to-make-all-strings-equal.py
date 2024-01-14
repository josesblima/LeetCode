class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        tlen = sum(len(word) for word in words)
        tlenrem = tlen % len(words)
        res = None
        vaj = {}
        prevvjkey = None
        if tlenrem != 0:
            return False
        if len(words) <= 1:
            return True
        for word in words:
            for char in word:
                if char in vaj:
                    vaj[char] = vaj[char] + 1
                else:
                    vaj[char] = 1
        firstvjj = list(vaj.values())[0]
        print(vaj)
        for vj_val in vaj.values():
            if vj_val % len(words) != 0:
                return False        
        return True
        




    
    print(makeEqual(1, ["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]
))


        