# Definition for singly-linked list.
# 내 풀이, 연결리스트 - 리스트 변환 인터넷 참고
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        lst=[]
        lstnode = None
        node = l1
        while node is not None:
            lst.append(node.val)
            node = node.next
        node = l2
        while node is not None:
            lst.append(node.val)
            node = node.next
        lst.sort()
        while lst:
            lstnode = ListNode(lst.pop(), lstnode)
        return lstnode
        