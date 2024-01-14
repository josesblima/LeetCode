# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        global avg_list
        avg_list = []
        level = 0
        res = []
        def bfs(root, level):
            # Tries to append val to list
            try:
                avg_list[level].append(root.val)
            # Creates list inside the list
            # and then appends val to list
            except:
                avg_list.append([])
                avg_list[level].append(root.val)
            # Go one level lower and increase level    
            if root.left != None:
                bfs(root.left, level + 1)
            if root.right != None:
                bfs(root.right, level + 1)
        bfs(root, level)     
        # Checks avg of each level
        for lvl in avg_list:
            res.append(sum(lvl) / len(lvl))
        return res
        