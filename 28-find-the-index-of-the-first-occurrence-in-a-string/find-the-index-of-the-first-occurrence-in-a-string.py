class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        i, size = 1, 0
        while i < len(needle):
            if needle[i] == needle[size]:
                lps[i] = size + 1
                size += 1; i += 1
            else:
                if size == 0:
                    lps[i] = 0
                    i += 1
                else:
                    size = lps[size - 1]
        print(lps)
        i = 0; n = 0     
        while i < len(haystack) and n < len(needle):
            if haystack[i] == needle[n]:
                i += 1; n += 1
            else:
                if n == 0:
                    i += 1
                else:
                    n = lps[n - 1]
            if n == len(needle):
                print(i - len(needle))
                return i - len(needle)
        print(-1)
        return -1
    strStr(1, haystack = "isissippi", needle = "issip")