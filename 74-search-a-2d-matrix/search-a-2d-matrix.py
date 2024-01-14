class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        mlists = sum(matrix, []) 
        print(mlists)
        left = 0
        right = len(mlists) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if mlists[midpoint] < target:
               left = midpoint + 1
            elif mlists[midpoint] > target:
               right = midpoint - 1
            elif mlists[midpoint] == target:
                print(True)
                return True
        print(False)    
        return False
    searchMatrix(1, [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 10)