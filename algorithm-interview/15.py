# 역순 연결 리스트로만 풀이한 나의 풀이 

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        dummy = ListNode(head.val, None)
        prev = dummy
        curr = head.next
        
        while curr:
            prev, prev.next, curr = curr, prev, curr.next

        return prev