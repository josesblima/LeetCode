class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dic = {}
        nochange = 0
        for x in range(len(s)):
            try:
                s_dic[s[x]] += 1
            except:
                s_dic[s[x]] = 1
            print(s_dic[s[x]])
        for z in range(len(t)):
            if t[z] in s_dic:
                if s_dic[t[z]] > 0:
                    s_dic[t[z]] -= 1
                    nochange += 1
        res = len(s) - nochange
        return res


        
