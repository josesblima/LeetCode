# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        res = None
        def doubleBfs(original, cloned, target):
            nonlocal res
            if original == target:
                res = cloned
                return cloned
            if original.left != None:
                doubleBfs(original.left, cloned.left, target)
            if original.right != None:
                doubleBfs(original.right, cloned.right, target)
        doubleBfs(original, cloned, target)
        return res
        