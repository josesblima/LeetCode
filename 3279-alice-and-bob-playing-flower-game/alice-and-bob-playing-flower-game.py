class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        res = 0
        for x in range(1, n + 1):
            # If x is even we want all odd numbers from 1 to m
            if x % 2 == 0:
                if m % 2 != 0:
                    res += m // 2 + 1
                else:
                    res += m // 2

            # If x is odd we want all the even numbers from 1 to m
            elif x % 2 != 0 and m > 1:
                if m % 2 == 0:
                    res += m // 2
                if m % 2 != 0:
                    res += m // 2
        print(res)
        return res


    flowerGame(1, n = 4, m = 3)