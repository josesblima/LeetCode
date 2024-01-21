class Solution:
    def minimumCost(self, nums):
        res = nums[0]
        nums = nums[1:]
        res += min(nums)
        for i in range(len(nums)):
            if nums[i] == min(nums):
                nums.remove(nums[i])
                break
        res +=  min(nums)
        print(res)
        return res
    minimumCost(1, [5,4,3])