from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 책보다 조금 더 쉬운 재귀 구조 

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        dummy = ListNode()
        head = dummy
        
        if l1.val < l2.val:
            head.next = l1
            head.next.next = self.mergeTwoLists(l1.next, l2)
        else:
            head.next = l2
            head.next.next = self.mergeTwoLists(l1, l2.next)
            

        return dummy.next