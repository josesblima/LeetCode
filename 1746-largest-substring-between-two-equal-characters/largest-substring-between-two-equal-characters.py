class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        largest_sstr = None
        for x in s:
            if s.find(x) != s.rfind(x): # and largest_sstr < s.rfind(x) - (s.find(x) + 1) or largest_sstr == None:
                if largest_sstr == None:
                    largest_sstr = s.rfind(x) - (s.find(x) + 1)
                if largest_sstr < s.rfind(x) - (s.find(x) + 1):
                    largest_sstr = s.rfind(x) - (s.find(x) + 1)
        print(largest_sstr)
        if largest_sstr == None:
            largest_sstr = -1 
        return largest_sstr
    maxLengthBetweenEqualCharacters(1, 'asa')


        