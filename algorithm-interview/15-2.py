# iterative

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # if head is None:
        #     return head 
        # prev를 None으로 설정하면 if문 안 써도 됨
        
        # dummy = ListNode(head.val, None) # ListNode로 새로 선언하지 않아도 됨
        prev = None
        node = head
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev