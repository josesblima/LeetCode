#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
# Whole issue is that if the substring is towards the end, 
# it keeps counting the potential as if you could extend s
class Solution:
    def characterReplacement(self, s, k):
        l, r, res = 0, 0, 0
        dic = {}
        ol = False
        while r < len(s):
            # Updates dictionary
            if s[r] in dic:
                if ol == False:
                    dic[s[r]] += 1
                remk = k - (r - l + 1 -dic[s[l]])
                # Updates res IF WITHIN BOUNDS, NEED TO IMPLEMENT STILL
                if remk <= len(s) - (r - l + 1):
                    if dic[s[l]] + k > res:
                        res = dic[s[l]] + k
                        print(res)
                else:  
                    if dic[s[l]] + len(s) - (r - l + 1) > res:
                        res = dic[s[l]] + len(s) - (r - l + 1)
                        print(res)
                      
            else:
                if ol == False:
                    dic[s[r]] = 1
                remk = k - (r - l + 1 -dic[s[l]])
                # Updates res IF WITHIN BOUNDS, NEED TO IMPLEMENT STILL
                if remk <= len(s) - (r - l + 1):
                    if dic[s[l]] + k > res:
                        res = dic[s[l]] + k
                        print(res)
                else:  
                    if dic[s[l]] + len(s) - (r - l + 1) > res:
                        res = dic[s[l]] + len(s) - (r - l + 1)
                        print(res)
            ol = False
            # Checks if there's higher potential and advances right
            if r < len(s) - 1 and r - l + 1 < dic[s[l]] + k:
                r += 1
                continue
            # If it's at the potential limit, checks if the next char
            # is the same as the left pointer and advances right
            elif r - l + 1 <= dic[s[l]] + k and r < len(s) - 1:
                if s[l] == s[r + 1]:
                    r += 1
                    continue
                # Or it advances left and right and removes left from dic
                else:
                    dic[s[l]] -= 1
                    l, r = l + 1, r + 1
                    continue
            # If len of l-r minus the amount of chars l is less than k
            # means that that number won't work so advance both
            elif r - l +1 - dic[s[l]] > k and r < len(s) - 1:
                dic[s[l]] -= 1
                l, r = l + 1, r + 1
                continue
            if r > l and r == len(s) - 1:
                dic[s[l]] -= 1
                l += 1
                ol = True
                continue
            break
        print(res)
        return res
    characterReplacement(1, "AAAAABBBBCBB", 4)
#                                ^               ^
        
# @lc code=end

