# 연결 리스트 -> 문자열 -> 정수로 계산 -> 문자열 -> 연결 리스트... 를 함수로 만들어서...
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        sum = int(''.join(str(e) for e in a)) + int (''.join(str(e) for e in b))
        
        return self.toReversedLinkedList(str(sum))

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 15-2 reverse 사용
        prev = None
        node = head
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def toList(self, node: List) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node