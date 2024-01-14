# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        cur1 = list1
        cur2 = list2
        res = []
        while cur1 != None and cur2 != None:
            while cur1 != None and cur2 != None and cur1.val <= cur2.val:
                res.append(cur1.val)
                cur1 = cur1.next
            while cur2 != None and cur1 != None and cur2.val <= cur1.val:
                res.append(cur2.val)
                cur2 = cur2.next
        while cur1 != None:
            res.append(cur1.val)
            cur1 = cur1.next
        while cur2 != None:
            res.append(cur2.val)
            cur2 = cur2.next

        fres = ListNode()
        if len(res) <= 0:
            return None
        fres.val = res[0]
        cur1 = fres
        
        for elems in res[1:]:
            cur1.next = ListNode()
            cur1.next.val = elems
            print(cur1.next.val)
            cur1 = cur1.next
        return fres
            

        