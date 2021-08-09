# Definition for singly-linked list.
# 내 풀이인데, LinkNode를 활용한다면 배열을 사용하지 않는 효율적인 풀이가 있을 것 같다.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        head_list = []
        now = head
        while True:
            head_list.append(now.val)
            if now.next != None: 
                now = now.next
                continue
            break
            
        if head_list == head_list[::-1]:
            return True
        else:
            return False