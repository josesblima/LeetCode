class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict = {}
        l = 0; r = 0
        match = 0
        res = ''
        right = True
        left = False
        for x in t:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        l, r = 0, 0
        while r < len(s):
            # We see what pointers we've previously moved and either add to
            # previous left or remove from new right and update match accordingly
            # You subtract dic entries until you reach 0 and then increase match
            if left == True:
                if s[l - 1] in dict:
                    dict[s[l - 1]] += 1
                    match -= 1 if dict[s[l - 1]] == 1 else 0
            if right == True:
                if s[r] in dict:
                    dict[s[r]] -= 1
                    match += 1 if dict[s[r]] == 0 else 0
            left, right = False, False
            # Increases right pointer until t is within it when we still have no result
            if match < len(dict) and res == '':
                r += 1
                right = True
                continue
            # Since we already have a res, we don't care about moving l or r individually
            # unless we get all the matches so we move both until we find them
            if match < len(dict) and res != '':
                l += 1; r += 1
                left, right = True, True
                continue
            # Here we already have all letters so we'll update res
            # and we see wether we can advance left, otherwise we move l and r
            if match == len(dict):
                res = s[l:r + 1]
                # if l in dict, we see if we can move left without it going losing the match
                if s[l] in dict:
                    if dict[s[l]] < 0:
                        l += 1
                        left = True
                        continue
                # If l isn't even part of dict, means we can advance left (not sure if necessary)
                l += 1
                left = True
        return res
    minWindow(1, 'bba', 'ab')