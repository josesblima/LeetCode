# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root) -> int:
        global divisor, total, lst
        res = 0
        total = 0
        lst = []
        # DFS and makes a list
        def subTitsAvg(root):
            nonlocal res
            lst.append(root.val)
            if root.left != None:
                subTitsAvg(root.left)
            if root.right != None:
                subTitsAvg(root.right)
                
        def traverseTitsAvg(root):
            global lst
            nonlocal res
            lst = []
            subTitsAvg(root)
            print(lst)
            if sum(lst) // len(lst) == root.val:
                res += 1
            if root.left != None:
                traverseTitsAvg(root.left)
            if root.right != None:
                traverseTitsAvg(root.right)
        traverseTitsAvg(root)
        return res
            
            

        