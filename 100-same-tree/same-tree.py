# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        global res
        res = True
        def lrcheck(pnode, qnode):
            global res
            if pnode != None and qnode == None:
                res = False
                return False
            if pnode == None and qnode != None:
                res = False
                return False
            if pnode == None and qnode == None:
                return True
            if pnode.val != qnode.val:
                res = False
                return False
            if res == True:
                return lrcheck(pnode.left, qnode.left) and lrcheck(pnode.right, qnode.right)
        pnode = p
        qnode = q
        lrcheck(pnode, qnode)
        return res
            
        