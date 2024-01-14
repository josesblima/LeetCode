from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums) -> int:
        cnums = Counter(nums)
        print(cnums)
        res = 0
        topfreq = 0
        counter = 0
        for keys, values in cnums.items():
            if values >= topfreq:
                topfreq = values
        for keys, values in cnums.items():
            if values == topfreq:
                counter += 1   
            
        print(topfreq)
        print(counter)
        return topfreq * counter
    maxFrequencyElements(1, [10,12,11,9,6,19,11])