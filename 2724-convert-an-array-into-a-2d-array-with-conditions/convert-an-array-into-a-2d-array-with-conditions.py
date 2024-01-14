from collections import Counter
class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        # Counts all occurences of numbers
        counter = Counter(nums)
        # Orders them
        mostcom = counter.most_common()
        counterlen = mostcom[0][1]
        # Creates lists inside a list equal to the highest occurence
        res = [[] for z in range(counterlen)]
        # First for loop to go over unique numbers,
        # second to distribute them through the lists
        for x in mostcom:
            for i in range(x[1]):
                res[i].append(x[0])    
        return res
    findMatrix(1, [8,8,8,8,2,4,4,2,4])
   
        