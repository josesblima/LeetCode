# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        carry = 0
        rescounter = 0
        res = []
        while cur1 != None and cur2 != None:
            res.append(cur1.val + cur2.val + carry)
            cur1 = cur1.next
            cur2 = cur2.next
            carry = 0
            if res[rescounter] > 9:
                st = str(res[rescounter])
                intitties = int(st[1])
                res[rescounter] = intitties
                carry +=1
            rescounter += 1
        while cur1 != None and cur2 == None:
            res.append(cur1.val + carry)
            cur1 = cur1.next
            carry = 0
            if res[rescounter] > 9:
                st = str(res[rescounter])
                intitties = int(st[1])
                res[rescounter] = intitties
                carry +=1
            rescounter += 1
        while cur1 == None and cur2 != None:
            res.append(cur2.val + carry)
            cur2 = cur2.next
            carry = 0
            if res[rescounter] > 9:
                st = str(res[rescounter])
                intitties = int(st[1])
                res[rescounter] = intitties
                carry +=1
            rescounter += 1
        if carry == 1:
            res.append(1)
        resl = ListNode()
        cur3 = resl
        if len(res) != 0:
            cur3.val = res[0]
            for x in res[1:]:
                cur3.next = ListNode()
                cur3.next.val = x
                cur3 = cur3.next
        


        return resl 



