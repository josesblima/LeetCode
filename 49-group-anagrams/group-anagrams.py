#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs):
        sorted_list = []
        word_index_dic = {}
        res = []
        # Create list with alphabetically sorted words
        for x in strs:
            sorted_word = ''.join(sorted(x))
            sorted_list.append(sorted_word)
        # Create dictionary with sorted word as value
        # and original words as keys
        for index, word in enumerate(sorted_list):
            if word in word_index_dic:
                word_index_dic[word].append(strs[index])
            else:
                word_index_dic[word] =[strs[index]]
        # Iterates through each key and their values and
        # passes the values do the final result
        for key in word_index_dic:
            res.append([])
            for orig_word in word_index_dic.get(key):
                res[-1].append(orig_word)
        return res
    groupAnagrams(1, ["eat","tea","tan","ate","nat","bat"])

        
        
# @lc code=end

