# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pos = set()
        cur1 = headA
        while cur1 != None:
            pos.add(cur1)
            cur1 = cur1.next
        cur2 = headB
        while cur2 != None:
            if cur2 in pos:
                return cur2
            cur2 = cur2.next
        return None   