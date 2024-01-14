# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        if root == None:
            return 0
        level = 1
        leaf = []
        # Traverses that shit and appends
        # the level of each leaf
        def smolTit(root, level):
            if root.left == None and root.right == None:
                leaf.append(level)
            if root.left != None:
                smolTit(root.left, level + 1)
            if root.right != None:
                smolTit(root.right, level + 1)
        smolTit(root, level)
        # checks for smolest leaf
        res = min(leaf)
        return res

        