class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prevx = 0
        curx = 0
        res = []
        for x in nums:
            curx = x + prevx
            res.append(curx)
            prevx = curx
        return res


