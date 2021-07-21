class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        # 파이썬에서는 배열의 reverse() 함수를 사용하면 배열을 거꾸로 뒤집기 가능

s = Solution()
print(s.reverseString(["h","e","l","l","o"]))