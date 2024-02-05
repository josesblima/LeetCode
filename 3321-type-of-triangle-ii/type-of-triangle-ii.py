class Solution:
    def triangleType(self, nums) -> str:
        prevx = nums[0]
        equilateral = True
        s = set()
        repetition = 0
        # Equilateral check
        for x in range(1, 3):
            if nums[x] != prevx:
                equilateral = False
            
        if equilateral == True:
            print('equilateral')
            return 'equilateral'
        
        # Check if it's scalene
        if nums[0] < nums[1] + nums[2]:
            if nums[0] in s:
                repetition += 1
            else:    
                s.add(nums[0])
        else:
            return 'none'
        if nums[1] < nums[0] + nums[2]:
            if nums[1] in s:
                repetition += 1
            else:    
                s.add(nums[1])
        else:
            return 'none'
        if nums[2] < nums[0] + nums[1]:
            if nums[2] in s:
                repetition += 1
            else:    
                s.add(nums[2])
        else:
            return 'none'
        if repetition == 1:
            return 'isosceles'
        else:
            return 'scalene'

        



    triangleType(1, [3,3,3])
        