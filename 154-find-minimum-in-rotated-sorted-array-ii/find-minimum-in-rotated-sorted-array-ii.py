class Solution:
    def findMin(self, nums: list[int]) -> int:
        global res
        res = None
        if nums[0] < nums[len(nums) - 1]:
            print(nums[0])
            return nums[0]
        elif len(nums) == 1:
            return nums[0]
        def binarySearchBreakPoint(left, right):
            global res
            midpoint = (right + left) // 2
            if left == right - 1 and nums[left] >= nums[right]:
                if res == None:
                    res = right
                    return res
                else:
                    if nums[res] > nums[right]:
                        res = right
                    return res

            elif nums[left] > nums[midpoint]:
                binarySearchBreakPoint(left, midpoint)
            elif nums[midpoint] > nums[right]:
                binarySearchBreakPoint(midpoint, right)
            elif left < right - 1:
                binarySearchBreakPoint(left, midpoint)
                binarySearchBreakPoint(midpoint, right)
            
        binarySearchBreakPoint(0, len(nums) - 1)
        print(nums[res])
        return nums[res]
    findMin(1, [10,1,10,10,10]) 