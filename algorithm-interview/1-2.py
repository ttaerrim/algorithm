import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크 (양방향 큐) 선언
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        #팰린드롬 여부 판별
        while(len(strs)>1):
            if strs.popleft() != strs.pop():
            # deque의 pop()은 오른쪽 요소 제거, popleft()는 왼쪽 요소 제거, 배열의 맨 첫 번째 인덱스와 맨 마지막 인덱스 pop 하면서 비교!
                return False
        return True




s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))