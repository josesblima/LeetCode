#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        pos = set()
        cur = head
        while cur != None:
            if cur in pos:
                return True
            pos.add(cur)
            cur = cur.next

        

        