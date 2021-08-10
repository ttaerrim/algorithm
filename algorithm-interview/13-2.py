# deque 양방향 큐 이용하기 1-2.py 참고
import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = collections.deque()
        if not head:
            return True
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q)>1:
            if q.popleft() != q.pop():
                return False
        return True