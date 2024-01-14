# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        global finres
        finres = 0
        res = 0
        def treeDepth(root, res):
            global finres
            res += 1
            if root.left == None and root.right == None and finres < res:
                finres = res
                res = 0
                return finres
            else:
                if root.left != None:
                    treeDepth(root.left, res)
                if root.right != None:
                    treeDepth(root.right, res)
        if root != None:
            treeDepth(root, res)
        print(finres)
        return finres

        