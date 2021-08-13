# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        node = head
        new = None
        while node:
            lst.append(node.val)
            node = node.next
        lst.reverse()
        while lst:
            new = ListNode(lst.pop(), new)
        return new
        