class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = None
        nums_dic = {}
        index = 0
        for i in nums:
            if i in nums_dic:
                nums_dic[i].append(index)
            else:
                nums_dic[i] = [index]
            index += 1
        for x in nums_dic.keys():
            complement = target - x
            if complement in nums_dic and x != complement:
                result = [nums_dic[x][0], nums_dic[complement][0]]
                break
            elif complement in nums_dic and len(nums_dic[complement]) > 1:
                result = [nums_dic[x][0], nums_dic[x][1]]
        return result

       