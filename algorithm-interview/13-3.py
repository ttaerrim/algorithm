# 런너를 이용한 팰린드롬 연결 리스트
# 234. Palindrome Linked List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            # 파이썬 다중 할당이 중요한 코드
        if fast:
            slow = slow.next

        node = slow
        print("slow")
        while node is not None:
            print(node.val, end="->")
            node = node.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

lst=[1,2,2,1]
lstnode=None
while lst:
    lstnode = ListNode(lst.pop(), lstnode)
s = Solution()
s.isPalindrome(lstnode)