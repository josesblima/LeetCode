class Solution:
    def returnToBoundaryCount(self, nums) -> int:
        res = 0
        prevnumber = nums[0]
        if nums[0] > 0:
            prevnum = 'pos'
        else:
            prevnum = 'neg'
        for x in range(1, len(nums)):
            newnumber = prevnumber + nums[x]
            if prevnum == 'pos' and newnumber < 0:
                prevnum = 'neg'

            if prevnum == 'neg' and newnumber > 0:
                prevnum = 'pos'

            if newnumber == 0:
                res += 1
            prevnumber = newnumber
        return res
    returnToBoundaryCount(1, [2,3,-5])