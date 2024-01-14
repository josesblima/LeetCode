# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        global res
        res = 0
        def binTreeCheck(root):
            global res
            if root.val >= low and root.val <= high:
                res += root.val
            if root.left != None:
                binTreeCheck(root.left)
            if root.right != None:
                binTreeCheck(root.right)
        binTreeCheck(root)
        return res