class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wcount1 = {}
        wcount2 = {}
        # Make dictionaries
        for x in s:
            if x in wcount1:
                wcount1[x] += 1
            else:
                wcount1[x] = 1
        for x in t:
            if x in wcount2:
                wcount2[x] += 1
            else:
                wcount2[x] = 1
        # Check if they're the same/anagrams of each other
        if wcount1 == wcount2:
            return True
        return False
        