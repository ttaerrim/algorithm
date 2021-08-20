# 연결 리스트 -> 문자열 -> 정수로 계산 -> 문자열 -> 연결 리스트...
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1, num2 = "", ""
        result=None
        
        node = l1
        while node:
            s = str(node.val)
            num1 += s
            node = node.next
            
        node = l2
        while node:
            s = str(node.val)
            num2 += s
            node = node.next
        
        sum = str(int(num1[::-1])+int(num2[::-1]))
        
        
        for i in range(len(sum)):
            result = ListNode(sum[i], result)
        
        return result