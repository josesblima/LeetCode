class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        i = 0
        res = 0
        for x in range(len(word) // k):
            i += k
            res += 1
            if word[i:] == word[0:len(word) - i]:
                return res
        if len(word) % k == 0:
            return res
        else:
            res += 1
            return res



    minimumTimeToInitialState(1, "abacab", 4)   
        
        
    #abacaba
    #ba 12345
    #
    