import math
class Solution:
    def minEatingSpeed(self, piles, h):
        maximum = max(piles)
        l, r = 0, maximum

        while r != l + 1:
            midpoint = (l + r) // 2
            res = 0
            for x in piles:
                res += math.ceil(x/midpoint)
            # Go up
            if res <= h:
                r = midpoint
            # Go down
            if res > h:
                l = midpoint
        print(l, r)
        return r


    minEatingSpeed(1, piles = [3,6,7,11], h = 8)
