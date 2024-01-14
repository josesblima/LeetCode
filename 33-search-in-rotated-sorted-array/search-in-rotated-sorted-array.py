class Solution:
    def search(self, nums: list[int], target: int) -> int:
        breakpoint = 0
        left = 0
        right = len(nums) - 1
        if nums[left] > nums[right]:
            while left < right:
                midpoint = (left + right) // 2
                if nums[left] > nums[right] and right - left == 1:
                    breakpoint = right
                    break
                if nums[left] > nums[midpoint]:
                    right = midpoint
                elif nums[midpoint] > nums[right]:
                    left = midpoint
            print(breakpoint)
            nums = nums[breakpoint:] + nums[:breakpoint]
            print(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            midpoint = (left + right) // 2
            if nums[left] == target:
                print((left + breakpoint) % len(nums))
                return (left + breakpoint) % len(nums)
            elif nums[midpoint] == target:
                print((midpoint + breakpoint) % len(nums))
                return (midpoint + breakpoint) % len(nums)
            elif nums[midpoint] < target:
                left = midpoint + 1
            elif nums[midpoint] > target:
                right = midpoint - 1
        midpoint = (left + right) // 2
        if nums[midpoint] == target:
            print((midpoint + breakpoint) % len(nums))
            return (midpoint + breakpoint) % len(nums)
        print('-1')
        return -1
    search(1, [1,2,3,4], 6)



        