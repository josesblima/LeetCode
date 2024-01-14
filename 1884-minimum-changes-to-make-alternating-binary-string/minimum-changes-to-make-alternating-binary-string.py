class Solution:
    def minOperations(self, s: str) -> int:
        return min(sum(1 for i in range(len(s)) if str(i % 2) != s[i]), sum(1 for i in range(len(s)) if str(i % 2) == s[i]))