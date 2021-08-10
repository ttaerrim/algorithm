# 책에는 160ms라고 나와 있는데 실제 실행 런타임은 1300ms 정도 나온다. (아마 오타인 것 같기도)
# 나의 풀이는 이 리스트 변환 풀이와 비슷하다.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = []
        if not head:
            return True
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q)>1:
            if q.pop(0) != q.pop():
                return False
        return True