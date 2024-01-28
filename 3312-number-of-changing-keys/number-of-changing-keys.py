class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        if len(s) == 0:
            return 0
        change = 0
        prev = s[0]
        for x in s:
            if x != prev:
                change += 1
            prev = x
        return change