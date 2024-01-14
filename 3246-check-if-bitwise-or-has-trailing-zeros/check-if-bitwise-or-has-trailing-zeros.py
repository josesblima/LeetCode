class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        trailzero = []
        for x in nums:
            if bin(x)[-1] == '0':
                trailzero.append(x)
                print(trailzero)
        if len(trailzero) < 2:
            print(1)
            return False
        else:
            print(2)
            return True


    hasTrailingZeros(1, [1,2,3,4,5])