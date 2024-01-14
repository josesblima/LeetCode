from collections import Counter
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        count = Counter(nums)
        print(count)
        res = 0
        for num, freq in count.items():
            while freq > 0:
                if freq == 4:
                    res += 2
                    freq -= 4
                if freq == 2:
                    res += 1
                    freq -= 2
                if freq == 3 or freq > 4:
                    res += 1
                    freq -= 3
                if freq == 1:
                    res = -1
                    return res
        print(res)
        return res


    minOperations(1, [2,3,3,2,2,4,2,3,4])