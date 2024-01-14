class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        banklasers = [0] * len(bank)
        newbanklasers = []
        res = 0
        for row in range(len(bank)):
            for laser in bank[row]:
                if laser == '1':
                    banklasers[row] += 1
        for notzero in banklasers:
            if notzero != 0:
                newbanklasers.append(notzero)

        print(newbanklasers)
        for x in range(len(newbanklasers)):
            if x < len(newbanklasers) - 1:
                if newbanklasers[x+1] != 0:
                    res +=  newbanklasers[x] * newbanklasers[x+1]
        print(newbanklasers)
        print(res)
        return res



    numberOfBeams(1, ["011001","000000","000000","001011"])
        