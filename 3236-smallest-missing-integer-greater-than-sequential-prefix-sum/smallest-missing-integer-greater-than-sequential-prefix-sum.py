class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        seq = []
        res = []
        finres = 0
        for x in range(len(nums)):
            if len(seq) == 0:
                seq.append(nums[x])
            if len(seq) > len(res):
                res = seq
            if x == len(nums) -1:
                break
            if x < len(nums) - 1:
                if nums[x] == nums[x + 1] - 1:
                    seq.append(nums[x+1])
                    if len(seq) > len(res):
                        res = seq
                if nums[x] != nums[x+1] - 1:
                    break
        sumtotal = sum(res)
        for z in range(len(nums)):
            try:
                wer = nums.index(sumtotal)
                sumtotal += 1

            except:
                print(sumtotal)
                return sumtotal
        if finres == 0:
            finres = sumtotal   


        print(seq)
        print(res)
        print(finres)
        print(sumtotal)
        return finres
    missingInteger(1, [37,1,2,9,5,8,5,2,9,4])