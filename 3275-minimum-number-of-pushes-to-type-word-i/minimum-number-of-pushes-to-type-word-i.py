class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        ncount = 0
        click = 1
        for x in word:
            if ncount > 7:
                ncount = 0
                click += 1
            ncount += 1
            res += click
        print(res)
        return res


    minimumPushes(1, "xycdefghij")