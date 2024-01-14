class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        midpoint = (left + right) // 2 
        while left <= right:
            midpoint = (left + right) // 2 
            if nums[midpoint] < target:
                left = midpoint + 1
            elif nums[midpoint] > target:
                right = midpoint - 1
            elif nums[midpoint] == target:
                print(midpoint)
                return midpoint
        return -1


    search(1, [-1,0,3,5,9,12], 2)