#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        nums_dic = Counter(nums)
        sorted_nums = nums_dic.most_common()
        print(sorted_nums)
        res = []
        # Grabs the top k numbers
        print(nums_dic[0])
        for count, ele in enumerate(sorted_nums):
            if count >= k:
                print(res)
                return res
            res.append(ele[0])
        print(res)
        return res
    topKFrequent(1, [3,0,1,0], 3)
        
# @lc code=end

