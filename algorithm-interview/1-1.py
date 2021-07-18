class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        #팰린드롬 여부 판별
        while(len(strs)>1):
            if strs.pop(0) != strs.pop():
            # pop 함수는 인덱스 지정 가능, 배열의 맨 첫 번째 인덱스와 맨 마지막 인덱스 pop 하면서 비교!
                return False
        return True





s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))