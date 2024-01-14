# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        tree1 = []
        tree2 = []
        def treeSearch1(root):
            if root.left == None and root.right == None:
                tree1.append(root.val)
            if root.left != None:
                treeSearch1(root.left)
            if root.right != None:
                treeSearch1(root.right)
        def treeSearch2(root):
            if root.left == None and root.right == None:
                tree2.append(root.val)
            if root.left != None:
                treeSearch2(root.left)
            if root.right != None:
                treeSearch2(root.right)
        treeSearch1(root1)
        treeSearch2(root2)
        print('root1: ', tree1)
        print('root2: ', tree2)
        if tree1 == tree2:
            return True
        else:
            return False