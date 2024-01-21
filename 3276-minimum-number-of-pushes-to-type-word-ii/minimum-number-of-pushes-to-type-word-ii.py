from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        ncount = 0
        click = 1
        dic = {}
        freq = Counter(word)
        print(freq)
        mfreq = freq.most_common()
        print(mfreq)
        for l, f in mfreq:
            for x in range(f):
                if l in dic:
                    res += dic[l]
                else:
                    dic[l] = click
                    res += dic[l]
                    ncount += 1
                    if ncount > 7:
                        ncount = 0
                        click += 1
        
        print(res)
        return res
    minimumPushes(1, "aabbccddeeffgghhiiiiii")