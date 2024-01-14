class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        counter1 = 0
        counter2 = 0
        def vowelCheck(letter):
            
            if letter == 'a' or letter == 'e' or  letter == 'i' or letter == 'o' or letter == 'u':
                return True
        for x in range(len(s)):
            if vowelCheck(s[x]) and x < len(s) // 2:
                counter1 += 1
            if vowelCheck(s[x]) and x >= len(s) // 2:
                counter2 += 1
        if counter1 == counter2:
            return True
        return False