import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # 모두 소문자 변환
        s = re.sub('[^a-z0-9]', '', s) # 영문 소문자와 숫자를 제외한 문자는 제거
        
        
        return s == s[::-1] # [::-1]은 배열을 거꾸로 뒤집는 기능




s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))